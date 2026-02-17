# Aura-X Diagrams

These diagrams explain the **architecture**, **data-flow**, and **workflows** for Aura-X.

## 📐 Architecture & Workflows
👉 See full system diagrams here: [docs/diagrams.md](docs/diagrams.md)

---

## 1) System Architecture (High-Level)


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




