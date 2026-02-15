# Aura-X 

AI-powered multi-domain intelligence platform for Tourism, Mining, 
Municipal Operations, and Transport Corridors.

## Diagrams
- Full system architecture, data-flow, and workflows:
  👉 `docs/diagrams.md`


```mermaid
flowchart TB
  subgraph Users["Users / Stakeholders"]
    U1["Tourist / Citizen / Mine Supervisor"]
    U2["Operations Manager / Municipality"]
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
    ORCH["AuraXOrchestrator\n(YAML-driven workflow engine)"]
    YAML["Workflows (YAML)\n- tourism_intelligence.yaml\n- mining_safety.yaml\n- municipal_ops.yaml\n- tourism_* clusters\n- rail_corridor_tourism.yaml"]
    AGENTS["Agents\nTourism / Mining / Municipal\nReasoning / Recommend / Response\nMonitoring"]
    LLM["LLM Adapter (optional)\nOpenAI now → Huawei later"]
  end

  subgraph Outputs["Outputs"]
    JSON["Structured Output JSON\n(schema_version 1.0)"]
    RUNS["Runs Archive\n/runs/*.json"]
  end

  subgraph Huawei["Huawei Cloud (Deployment & Ops)"]
    ECS["ECS / CCE\n(Host API)"]
    OBS["OBS\n(Store runs & media)"]
    LTS["LTS\n(Log shipping / auditing)"]
    CloudEye["Cloud Eye\n(Metrics + alerts)"]
    IAM["IAM\n(Access control)"]
  end

  Users --> Client
  Client --> API
  API --> Core
  YAML --> ORCH
  ORCH --> AGENTS
  AGENTS --> LLM
  ORCH --> JSON
  JSON --> RUNS

  API -.deploy.-> Huawei
  RUNS -.archive.-> OBS
  API -.logs.-> LTS
  API -.metrics.-> CloudEye
  Huawei -.secure.-> IAM

sequenceDiagram
  autonumber
  participant User as User / Client
  participant API as FastAPI (/run)
  participant Orchestrator as AuraXOrchestrator
  participant Agents as Agents (Analyze/Reason/Recommend/Respond)
  participant LLM as LLM Adapter (optional)
  participant Runs as runs/*.json
  participant Huawei as Huawei Cloud (OBS/LTS)

  User->>API: POST /run (workflow + inputs)
  API->>Orchestrator: orchestrator.run(inputs)
  Orchestrator->>Agents: Execute YAML steps in order

  Agents->>LLM: call_openai(...) [optional]
  LLM-->>Agents: reasoning text / structured hints

  Agents-->>Orchestrator: step outputs
  Orchestrator-->>API: structured JSON output
  API-->>User: response JSON

  Orchestrator->>Runs: save JSON run artifact
  Runs-->>Huawei: (future) sync to OBS
  API-->>Huawei: (future) logs to LTS + metrics to Cloud Eye

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

