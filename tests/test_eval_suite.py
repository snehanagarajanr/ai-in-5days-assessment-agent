"""Automated evaluation test harness measuring agent quality against a golden dataset."""

import unittest
from agent.tools import create_critical_incident_ticket, CreateCriticalBugInput
from agent.orchestrator import strategic_model_router, policy_guardrail_validator


class TestAgentEvaluationHarness(unittest.TestCase):
    """Measures deterministic tool execution and reasoning routing against golden test cases."""

    def setUp(self):
        self.golden_dataset = [
            {
                "service": "auth-service",
                "severity": "P0",
                "summary": "503 Service Unavailable on token endpoint",
                "expected_status": "CREATED"
            },
            {
                "severity": "billing-pipeline",
                "severity": "P1",
                "summary": "PubSub message latency exceeds 1500ms SLO",
                "expected_status": "CREATED"
            }
        ]

    def test_golden_dataset_ticket_creation(self):
        for sample in self.golden_dataset:
            payload = CreateCriticalBugInput(
                service_name=sample["service"],
                severity_level=sample["severity"],
                root_cause_summary=sample["summary"]
            )
            result = create_critical_incident_ticket(payload)
            self.assertEqual(result["status"], sample[
expected_status"])
            self.assertEqual(result["severity"], sample["severity"])

    def test_model_routing_logic(self):
        self.assertEqual(strategic_model_router("triage_summary"), "gemini-1.5-flash")
        self.assertEqual(strategic_model_router("deep_root_cause_analysis"), "gemini-1.5-pro")

    def test_guardrail_policy_enforcement(self):
        self.assertTrue(policy_guardrail_validator("Safely drain traffic from canary"))
        self.assertFalse(policy_guardrail_validator("Execute DROP TABLE users on database"))


if __name__ == "__main__":
    unittest.main()
