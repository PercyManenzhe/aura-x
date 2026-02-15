# Aura-X: AI-Powered 2D/3D/4D Virtual Tourism System

## Overview
Aura-X is an **immersive virtual tourism and industrial safety system** using 2D/3D/4D glasses, AI agents, and Huawei Cloud integration.  
It allows users to experience:

- Natural and cultural sites (Mpumalanga, township/village locations)  
- Industrial environments (mines, trains) with safety simulations  
- Multi-sensory immersion (visual, audio, haptic feedback)  

---

## Key Features

- **AI Agents**: Orchestrates tourism experiences and industrial safety modules  
- **LLM Service**: Generates dynamic content and guidance  
- **Huawei Cloud Adapter**: Mock integration for scalable cloud deployment  
- **Multi-mode Simulation**: 2D, 3D, 4D immersive environments  
- **Expandable**: Future AR/VR and multi-user collaboration  

---

## Project Structure

aura-x/
├── app/
│ ├── agents/ # AI Agents and Orchestrator
│ ├── api/ # FastAPI endpoints (future)
│ └── services/ # LLM and Cloud adapter
├── data/ # Demo content & scenarios
├── tests/ # Unit tests
├── run.py # Main entry point
├── requirements.txt # Dependencies
└── README.md

## System Architecture
![Aura-X Architecture](assets/diagrams/architecture/aura-x-system-architecture.png)

## Workflow Orchestration
![Tourism Workflow](assets/diagrams/workflows/tourism-workflow.png)
