# Enterprise Cloud Incident & Mitigation Agent

An autonomous incident management and root-cause analysis agent built for the **AI in 5 Days Assessment**.

## Architecture & Rubric Alignment

- **Tool & Interface Design:** Strictly typed with Pydantic schemas (`agent/tools.py`), descriptive names, and guided recovery error feedback.
- **Context & Memory:** Constitution prompt, sliding-window compaction to prevent context bloat, and asynchronous background persistence (`agent/memory.py`).
- **Orchestration & Logic:** Strategic model routing (Gemini 1.5 Flash vs Pro), safety policy guardrails, and Human-in-the-Loop authorization stops (`agent/orchestrator.py`).
- **Observability & Tracing:** OpenTelemetry distributed tracing spans, structured JSON event logging, and active PII/secret scrubbing (`agent/observability.py`).
- **Infrastructure & CI/CD:** Golden evaluation dataset harness (`tests/test_eval_suite.py`) and Terraform IaC with Secret Manager secret injection (`terraform/main.tf`).
