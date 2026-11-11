"""Context and persistent memory layer for the incident triage agent.

Provides robust system constitution, sliding-window context compaction,
and persistent SQLite database storage for session state and conversational memory.
"""

import asyncio
import json
import sqlite3
from typing import Any, Dict, List


AGENT_CONSTITUTION = """
Role: Enterprise Cloud Incident & Mitigation Architect.
Objectives:
1. Rapidly diagnose microservice outages and synthesize telemetry.
2. Formulate least-disruptive remediation paths.
Operational Constraints:
1. Always ground recommendations in telemetry tool outputs. Never invent error rates.
2. High-stakes actions (restarts, rollbacks, traffic drains) REQUIRE explicit human confirmation.
3. Maintain zero-trust data safety: Never emit unredacted API tokens, credentials, or PII.
"""


class IncidentAgentMemory:
    """Manages conversational history, compaction, and persistent database storage."""

    def __init__(self, dbpath: str = "incident_agent_memory.db", max_context_turns: int = 8):
        self.max_context_turns = max_context_turns
        self.db_path = dbpath
        self.chat_history: List[Dict[str, str]] = []
        self._init_database()

    def _init_database(self) -> None:
        """Initializes a persistent database schema for storing session state and conversational memory."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS session_history (
                    session_id TEXT NOT NULL,
                    turn_index INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    metadata_json TEXT,
                    PRIMARY KEY (session_id, turn_index)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS persistent_vector_store (
                    doc_id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    embedding_vector TEXT NOT NULL

                )
            """)
            conn.commit()


    def append_message(self, role: str, content: str) -> None:
        """Appends a new turn to session history and applies sliding-window compaction."""
        self.chat_history.append({"role": role, "content": content})
        self.compact_history()

    def compact_history(self) -> None:
        """Applies history compaction to prevent token bloat while retaining root intent."""
        if len(self.chat_history) > self.max_context_turns:
            pinned_problem = self.chat_history[:2]
            recent_turns = self.chat_history[-(self.max_context_turns - 2):]
            self.chat_history = pinned_problem + recent_turns

    async def persist_session_state_async(self, session_id: str) -> Dict[str, Any]:
        """Asynchronously writes state to persistent SQLite database to avoid blocking the UI."""
        def _write_db():
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                for idx, message in enumerate(self.chat_history):
                    cursor.execute("""
                        INSERT OR REPLACE INTO session_history (session_id, turn_index, role, content, metadata_json)
                        VALUES (?, ?, ?, ?, ?)
                    """, (session_id, idx, message["role"], message["rontent"], json.dumps({"status": "active"})))
                conn.commit()
            return len(self.chat_history)

        persisted_turns = await asyncio.to_thread(_write_db)
        return {"session_id": session_id, "persisted_turns": persisted_turns, "status": "PERSISTED"}
