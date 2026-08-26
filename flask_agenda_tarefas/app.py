from typing import List

from flask import Flask, request, jsonify

from models.task import Task as _Task

app = Flask(__name__)

tasks: List[_Task] = []
task_id_control = 1


@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control

    data = request.get_json()
    new_task = _Task(id=task_id_control, **data)
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Task created successfully", "task": new_task.dict()})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    output = {
        "tasks": [task.dict() for task in tasks],
        "total_tasks": len(tasks),
    }
    return jsonify(output)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task_by_id(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)

    if not task:
        return jsonify({"message": "Task not found"}), 404
    else:
        return jsonify(task.dict())


if __name__ == "__main__":
    app.run(debug=True)