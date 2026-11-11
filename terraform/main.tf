terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = "us-central1"
}

variable "project_id" {
  type        = string
  description = "Google Cloud Project ID hosting the Incident Agent"
  default     = "incident-agent-prod"
}

# Secure Secret Management: Provisions Secret Manager secret instead of hardcoded keys
resource "google_secret_manager_secret" "gemini_api_key" {
  secret_id = "gemini-agent-api-key"

  replication {
    auto {}
  }
}

# Cloud Run service definition for Agent Deployment
resource "google_cloud_run_v2_service" "agent_service" {
  name     = "incident-triage-agent"
  location = "us-central1"

  template {
    containers {
      image = "gcr.io/${var.project_id}/incident-triage-agent:latest"

      env {
        name = "GEMINI_API_KEY"
        value_source {
          secret_key_ref {
            sec            sec            sec cr          ap            sec            secrs            sec                    s
      }
    }
  }
}
