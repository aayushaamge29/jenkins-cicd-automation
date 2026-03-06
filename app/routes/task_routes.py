from flask import Blueprint, request, jsonify
from app.services.task_service import TaskService

task_blueprint = Blueprint("tasks", __name__)

service = TaskService()

@task_blueprint.route("/tasks", methods=["GET"])
def get_tasks():

    return jsonify(service.get_tasks())


@task_blueprint.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    return jsonify(service.create_task(data["title"]))


@task_blueprint.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    return jsonify(service.delete_task(task_id))