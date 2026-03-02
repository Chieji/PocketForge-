# Facebook AI Operator

A multi-agent system designed for automated Facebook operations using AI and browser automation.

## Architecture

### Cloud Brain
- **Type**: AI Planner + Memory Engine
- **Model Provider**: OpenAI
- **Functions**:
  - Task Planning
  - Content Generation
  - Long Term Memory
  - Error Recovery
  - Style Modeling
- **Deployment**: Docker on AWS/GCP

### Local Executor
- **Type**: Browser Automation Agent
- **Framework**: Playwright, FastAPI
- **Responsibilities**:
  - Execute UI Actions
  - Capture Screenshots
  - DOM Parsing
  - Session Control

### Browser Extension
- **Framework**: React
- **Functions**:
  - User Command Interface
  - Secure Tunnel to Local Agent
- **Permissions**: activeTab, storage, scripting

## Execution Flow
1. User sends command via Extension.
2. Local Agent forwards task to Cloud Brain.
3. Cloud Brain returns structured execution plan.
4. Local Executor performs Playwright actions.
5. Execution report sent back to Cloud.
6. Cloud updates memory + optionally commits improvements to GitHub.

## Security
- Local-only credential storage.
- Encrypted tunnel between components.
- Zero Facebook password storage.
