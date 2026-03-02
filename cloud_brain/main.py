import os
import uuid
from flask import Flask, request, jsonify
from cloud_brain.planner import AIPlanner
from cloud_brain.memory import MemoryEngine
from cloud_brain.github_service import GitHubService

app = Flask(__name__)
planner = AIPlanner()
memory = MemoryEngine()
github = GitHubService()

@app.route('/plan', methods=['POST'])
def create_plan():
    data = request.json
    command = data.get('command')
    user_id = data.get('user_id')

    context = memory.get_context(command)
    style = memory.get_style(user_id)

    plan = planner.generate_plan(command, context)

    # Execution Flow Step 4: If code change required -> Commit to GitHub
    for step in plan.get('steps', []):
        if step.get('action') == 'code_change':
            branch_name = f"auto-improve-{uuid.uuid4().hex[:8]}"
            github.create_branch(branch_name)
            github.commit_change(
                branch_name,
                step['file'],
                "# Auto-improved code content",
                f"Auto-improvement for {command}"
            )
            github.create_pull_request(
                f"Auto-improvement for {command}",
                "Self-improving code refactor",
                branch_name
            )

    return jsonify(plan)

@app.route('/report', methods=['POST'])
def receive_report():
    data = request.json
    event_id = data.get('event_id')
    execution_result = data.get('result')

    memory.store_event(event_id, execution_result)
    return jsonify({"status": "received", "event_id": event_id})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
