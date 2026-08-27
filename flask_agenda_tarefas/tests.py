from typing import List

import requests

from models.task import Task as _Task

BASE_URL = "http://127.0.0.1:5000"
tasks: List[_Task] = []


def test_create_task():
    new_task_data = {"title": "Nova Tarefa", "description": "Test Descrição da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Task created successfully"
    assert response_data["task"]["title"] == new_task_data["title"]
    assert response_data["task"]["description"] == new_task_data["description"]
    assert response_data["task"]["completed"] is False
    tasks.append(_Task(**response_data["task"]))


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["total_tasks"] == len(tasks)


def test_get_task_by_id():
    task = tasks[0]
    response = requests.get(f"{BASE_URL}/tasks/{task.id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == task.id
    assert response_data["title"] == task.title
    assert response_data["description"] == task.description
    assert response_data["completed"] == task.completed


def test_update_task_by_id():
    task = tasks[0]
    payload: _Task = _Task(task.id, "Nova Tarefa Atualizada", "Nova Descrição da Tarefa Atualizada", True)
    response = requests.put(f"{BASE_URL}/tasks/{task.id}", json=payload.dict())
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Task updated successfully"
    assert response_data["task"]["title"] == payload.title


def test_delete_task_by_id():
    task = tasks[0]
    response = requests.delete(f"{BASE_URL}/tasks/{task.id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["message"] == "Task deleted successfully"