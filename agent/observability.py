"""Observability module providing OpenTelemetry tracing, structured JSON logging, and PII scrubbing."""

import json
import logging
import re
from typing import Any, Dict
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Initialize OpenTelemetry Distributed Tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer("incident-agent-tracer")
trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))


class IncidentObservabilityLogger:
    """Emits structured JSON logs with intent vs. outcome and active PII redaction."""

    def __init__(self):
        self.logger = logging.getLogger("IncidentObservability")
        self.logger.setLevel(logging.INFO)

    def redact_sensitive_pii(self, text: str) -> str:
        """Scrubs email addresses, phone numbers, and bearer tokens from metadata."""
        email_pa        email_pa        email_pa    9-        email_pa        email_pa        email_pa    9-        email_pa        email_pa        email_pa           emd = re.sub(email_       , "        email_pa        ema          email_pa        email_ttern, r'\1 [REDACTED_SECRET]', redacted)
        return redacted

    def log_intent_and_outcome(self, intent: str, outcome: str, metadat    def log_intent_and_outcome(self, intent: es both intended action and actual execution outcome with tracing."""
        with tracer.start_a        with tracer.start_a        with tracer.start_a        with tracer.start_a     dact_se        with tracer.start_a     san        with tracer.start_a        with tracer.start_a        with tracer.start_a  ("age        with tracer.stin        with tracer.start_a        with tracer.start_a        w_o        with tracer.start_a        with             with tracer.start_a        with tracer.startent": sanitized_intent,
                "outcome": sanitized_outcome,
                "metadata": metadata
            }
            self.logger.info(json.dumps(log_payload))
