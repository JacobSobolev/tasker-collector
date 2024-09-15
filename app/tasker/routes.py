from flask import Blueprint, request

tasker_bp = Blueprint("tasker",__name__, url_prefix="/tasker")

TASK_TYPES = {"sum": 2, "multiply": 3}

def get_json_task():
    try:
        task = request.json["task"]
    except KeyError:
        return {"error": "no task provided"}
    if task not in TASK_TYPES:
        return {"error": "task not supported"}
    return task

@tasker_bp.route("/", methods=["POST"])
def do_task():
    task = get_json_task()
    if "error" in task:
        return task, 400
    return "ok"

@tasker_bp.route("/")
def show_tasks():
    return "all the tasks"