# Aura-X Diagrams

These diagrams explain the **architecture**, **data-flow**, and **workflows** for Aura-X.

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
    YAML["Workflows YAML\n- tourism_intelligence.yaml\n- mining_safety.yaml\n- municipal_ops.yaml\n- tourism_* clusters\n- rail_corridor_tourism.yaml"]
    AGENTS["Agents\nTourism / Mining / Municipal\nReasoning / Recommend / Response\nMonitoring"]
    LLM["LLM Adapter (optional)\nOpenAI now → Huawei later"]
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



sequenceDiagram
  autonumber
  participant User as User
  participant API as FastAPI
  participant Orchestrator as Orchestrator
  participant Agents as Agents
  participant LLM as LLM_Adapter
  participant Runs as Runs_JSON
  participant Huawei as Huawei_Cloud

  User->>API: POST /run (workflow + inputs)
  API->>Orchestrator: run(inputs)
  Orchestrator->>Agents: Execute YAML steps in order

  Agents->>LLM: call_openai() [optional]
  LLM-->>Agents: reasoning / structured hints

  Agents-->>Orchestrator: step outputs
  Orchestrator-->>API: structured JSON output
  API-->>User: response JSON

  Orchestrator->>Runs: save JSON run artifact
  Runs-->>Huawei: (future) sync to OBS
  API-->>Huawei: (future) logs to LTS + metrics to CloudEye


flowchart LR
  A["Analyze (TourismAgent)"] --> B["Reason (ReasoningAgent)"]
  B --> C["Recommend (RecommendationAgent)"]
  C --> D["Respond (ResponseAgent)"]
  D --> E["Monitor (MonitoringAgent)"]



flowchart LR
  A["Analyze (MiningSafetyAgent)"] --> B["Reason (ReasoningAgent)"]
  B --> C["Recommend (MiningRecommendationAgent)"]
  C --> D["Respond (ResponseAgent)"]
  D --> E["Monitor (MonitoringAgent)"]



flowchart LR
  A["Analyze (MunicipalOpsAgent)"] --> B["Reason (ReasoningAgent)"]
  B --> C["Recommend (MunicipalRecommendationAgent)"]
  C --> D["Respond (ResponseAgent)"]
  D --> E["Monitor (MonitoringAgent)"]




