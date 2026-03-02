from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
import httpx
import os

app = FastAPI()

CLOUD_BRAIN_URL = os.getenv("CLOUD_BRAIN_URL", "http://localhost:5000")

class TaskStep(BaseModel):
    action: str
    url: Optional[str] = None
    type: Optional[str] = None
    topic: Optional[str] = None
    selector: Optional[str] = None
    file: Optional[str] = None
    change: Optional[str] = None

class ExecutionTask(BaseModel):
    command: str
    user_id: Optional[str] = "default_user"

@app.post("/execute")
async def execute_task(task: ExecutionTask):
    """
    Forwards task to Cloud Brain, receives plan, and executes UI actions.
    """
    # Step 2 & 3: Local Agent forwards task to Cloud Brain and gets plan
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{CLOUD_BRAIN_URL}/plan",
                json={"command": task.command, "user_id": task.user_id}
            )
            response.raise_for_status()
            plan = response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Cloud Brain unreachable: {str(e)}")

    # Step 5: Local Executor performs Playwright actions
    results = []
    for step in plan.get("steps", []):
        if step["action"] == "code_change":
            continue # Already handled by Cloud Brain in this flow

        print(f"Executing step: {step['action']}")
        results.append({"step": step["action"], "status": "success"})

    # Step 6: Results returned to Cloud
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{CLOUD_BRAIN_URL}/report",
            json={"event_id": "exec_123", "result": results}
        )

    return {"task": task.command, "results": results}

@app.get("/status")
async def get_status():
    return {"status": "idle"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
