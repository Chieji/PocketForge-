import os
from flask import Flask, request, jsonify
from .planner import AIPlanner
from .memory import MemoryEngine

app = Flask(__name__)
planner = AIPlanner()
memory = MemoryEngine()

@app.route('/plan', methods=['POST'])
def create_plan():
    data = request.json
    command = data.get('command')
    user_id = data.get('user_id')

    context = memory.get_context(command)
    style = memory.get_style(user_id)

    plan = planner.generate_plan(command, context)
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
