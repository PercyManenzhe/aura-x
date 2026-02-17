## 🏗 System Design Philosophy

Aura-X follows a modular, YAML-driven, multi-agent architecture.

Design principles:
- Workflow-driven orchestration
- Agent specialization per domain
- Provider-agnostic LLM integration
- Structured outputs for auditability
- Cloud-native deployment readiness (Huawei Cloud)

# Aura-X Diagrams

These diagrams explain the **architecture**, **data-flow**, and **workflows** for Aura-X.

## Contents
- [Architecture & Workflows](#-architecture--workflows)
- [System Architecture (High-Level)](#-1-system-architecture-high-level)

## 📐 Architecture & Workflows
See full system diagrams in this document.

---

## 1) System Architecture (High-Level)

```mermaid
flowchart TB
  subgraph Users["Users & Stakeholders"]
    U1["Tourist / Citizen / Mine Supervisor"]
    U2["Ops Manager / Municipality"]
    U3["Judges / Investors"]
  end

  subgraph Client["Client Apps"]
    W["Web / Swagger UI (/docs)"]
    CLI["CLI Demo Scripts (demo.py / local_demo_*.py)"]
  end

  subgraph API["Aura-X API (FastAPI)"]
    ENDPOINTS["/health  /run"]
  end

  subgraph Core["Aura-X Core"]
    ORCH["AuraXOrchestrator (YAML workflow engine)"]
    YAML["Workflows YAML<br/>- tourism_intelligence.yaml<br/>- mining_safety.yaml<br/>- municipal_ops.yaml<br/>- tourism_* clusters<br/>- rail_corridor_tourism.yaml"]
    AGENTS["Agents<br/>Tourism / Mining / Municipal<br/>Reasoning / Recommend / Response<br/>Monitoring"]
    LLM["LLM Adapter (optional)<br/>OpenAI now → Huawei later"]
  end

  subgraph Outputs["Outputs"]
    JSON["Structured Output JSON (schema v1.0)"]
    RUNS["Runs Archive: /runs/*.json"]
  end

  subgraph Huawei["Huawei Cloud (Deployment & Ops)"]
    ECS["ECS / CCE (Host API)"]
    OBS["OBS (Store runs & media)"]
    LTS["LTS (Logs / audit trail)"]
    CloudEye["Cloud Eye (Metrics + alerts)"]
    IAM["IAM (Access control)"]
  end

  Users --> Client
  Client --> API
  API --> Core
  YAML --> ORCH
  ORCH --> AGENTS
  AGENTS --> LLM
  ORCH --> JSON
  JSON --> RUNS

  API -.deploy.-> ECS
  RUNS -.archive.-> OBS
  API -.logs.-> LTS
  API -.metrics.-> CloudEye
  Huawei -.secure.-> IAM
```

### Agent: Tourism — Purpose & context
- Purpose: generate tourism intelligence and recommendations.
- Trigger: YAML workflow "tourism_intelligence.yaml" via /run API.
- Inputs: location, user profile, historical runs.
- Outputs: structured JSON recommendations, alerts.
- Audience: Ops managers, tourism analysts.
- Notes: fallback to LLM adapter if external reasoning required.

### Agent: Mining — Purpose & context
- Purpose: monitor mining-safety signals and produce risk assessments.
- Trigger: mining_safety.yaml workflows / sensor ingestion.
- Inputs: sensor telemetry, incident reports, schedules.
- Outputs: safety alerts, mitigation steps, run artifacts.
- Audience: Mine supervisors, safety engineers.
- Notes: enforce data-retention & audit via LTS/OBS.

### Agent: Municipal — Purpose & context
- Purpose: municipal operations recommendations and response planning.
- Trigger: municipal_ops.yaml workflows / scheduled runs.
- Inputs: municipal datasets, citizen reports.
- Outputs: operational plans, dispatch instructions.
- Audience: Municipality ops teams.
- Notes: integrate IAM-based access for sensitive data.

Short legend:
- Users: human stakeholders interacting with the system.
- Client: web/CLI entry points.
- API: FastAPI endpoints.
- Core: orchestrator, workflows, agents, LLM adapter.
- Outputs: structured run artifacts.
- Huawei: deployment/storage/ops services.

**LLM adapter — provider plan**
- OpenAI: used for initial prototyping.
- Huawei: planned for production (data‑residency / compliance).
Notes: implement a provider‑agnostic adapter; select provider via config/env var (e.g. AURA_X_LLM_PROVIDER). Document migration timeline and fallback behaviour in README/deployment docs.
