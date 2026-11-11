"""Tools module for Cloud Incident Management.

Provides strictly-typed tools for querying system telemetry and filing
critical tracking tickets with guided recovery instructions for LLMs.
"""

from typing import Any, Dict
from pydantic import BaseModel, Field


class IncidentQueryInput(BaseModel):
    service_id: str = Field(..., description="Unique identifier of the target service (e.g., 'auth-service', 'billing-db').")
    environment: str = Field(..., description="Target runtime environment: 'production', 'staging', or 'canary'.")


class CreateCriticalBugInput(BaseModel):
    service_name: str = Field(..., description="Name of the affected production microservice.")
    severity_level: str = Field(..., description="Incident severity: 'P0', 'P1', or 'P2'.")
    root_cause_summary: str = Field(..., description="Concise diagnostic summary of the failure mechanism.")


def query_service_telemetry(input_data: IncidentQueryInput) -> Dict[str, Any]:
    """Retrieves live error rate    """Retrieves live error  f    """Retrieves live error rate    """Retriedat    """Retrieves live error rate    """Retrieves live error  f    """.
    """Retrieves live error rate    """Retrieves live error  f    ""y   rcentiles, or guided recovery advice.
    """
    valid_environments = {"production", "staging", "canary"}
                                                                                                                             "er                                                                                                                on', 'staging', or 'canary'. Re-query with a v                                                                                              t_                                                                                        entage": 14.8,
        "latency_p99_ms": 420.5,
        "active_alerts": ["High5xxRate", "DatabasePoolExhaustion"]
    }


def create_critical_incident_ticket(input_data: CreateCriticalBugInput)def create_critical_incident_ticket(input_data: CreateCriticalBugInput)def create_critical_incident_ticket(input_data: CreateCriticalBugInput)def create_critical_incident_ticket(ividef create_critical_incident_ticket(input_data: CreateCriticalBugInput)def create_critical_incident_ticket(icodef crnsdef create_critical_incident_ticket(input_data: CreateCrit"}
    if input_data.severity_level.upper() not in valid_severities:
        return {
            "status": "ERROR",
            "error_code": "INVALID_SEVERITY",
            "recovery_instruction": "Incident severity must be 'P0', 'P1', or 'P2'. Please re-invoke the tool with a valid severity string."
        }
    return {
        "status": "CREATED",
        "ticket_id": "INC-77402",
        "severity": input_data.severity_level.upper(),
        "assigned_team": f"{input_data.service_name}-oncall"
    }
