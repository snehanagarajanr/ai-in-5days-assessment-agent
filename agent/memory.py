"""Context and memory layer for the incident triage agent.

Manages the system constitution, context compaction across multi-turn dialogs,
and non-blocking asynchronous state persistence.
"""

import asyncio
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
    """Manages conversational history, compaction, and async persistence."""

    def __init__(self, max_context_turns: int = 8):
        self.max_context_turns = max_context_turns
        self.chat_history        self.chat_history              self.chat_history        self.chat_history       ] =        self.chat_history        self.chat_history              self.chat_his""        self.chat_history        self.chat_histes slid        self.mp        self.chat_history     istory.        self.chat_his "co        self.chat_history        self.chat_history    def compact_hi        self.chat_history        self.chat_history              sve        self.chat_history        self.chat_h""
                      at_hi                      at_hi                      at_hi                      at_hi t + the most recent active dialogue turns
            pinned_problem = self.chat_history[:2]
                                                                                                  _history                         t_                                                                         > Dic                                               onver                                              ckground."""
        await asyncio.sleep(0.01)  # Non-blocking async datastore write simulation
        self.persisted_store[session_id] = list(self.chat_history)
        return {"session_id": session_id, "persisted_turns": len(self.chat_history), "status": "PERSISTED"}
