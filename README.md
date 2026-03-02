# Facebook AI Operator

A multi-agent system designed for automated Facebook operations using AI and browser automation.

## Architecture

### Cloud Brain
- **Type**: AI Planner + Memory + Self-Improving Engine
- **Model Provider**: OpenAI
- **Core Functions**:
  - Task Planning
  - Content Generation
  - Long Term Memory
  - Error Recovery
  - Style Modeling
- **Self-Improvement**:
  - Code Review Agent
  - Auto Refactor
  - Performance Analyzer
  - Auto Commit Improvements
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
- **Framework**: React + TypeScript
- **Functions**:
  - User Command Interface
  - Secure Tunnel to Local Agent
- **Permissions**: activeTab, storage, scripting

## GitHub Integration
- **Capabilities**:
  - Auto Commit Generated Code
  - Create Branches and Pull Requests
  - Issue Synchronization
  - Trigger CI Workflows

## Execution Flow
1. User sends command via Extension.
2. Local Agent forwards task to Cloud Brain.
3. Cloud Brain generates execution + code plan.
4. If code change required → Commit to GitHub.
5. Local Executor performs Playwright actions.
6. Execution report sent back to Cloud.
7. Memory + system refinement updated.

## Security
- Local-only credential storage.
- Encrypted tunnel between components.
- Zero Facebook password storage.
- Scoped GitHub access.
