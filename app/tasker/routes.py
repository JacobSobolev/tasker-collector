from flask import Blueprint, request
from ast import literal_eval

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

def get_json_params(task):
    try:
        params = literal_eval(request.json["params"])
        # params = request.json["params"]
    except KeyError:
        return {"error": "no params provided"}
    except ValueError:
        return {"error": "params needs to be a list"}
    if not isinstance(params, list):
        return {"error": "params needs to be a list"}
    if not all(isinstance(item, int) for item in params):
        return {"error": "list needs to be only int"}
    if not TASK_TYPES[task] == len(params):
        return {"error": "list not in the correct size"}
    return params

@tasker_bp.route("/", methods=["POST"])
def do_task():
    task = get_json_task()
    if "error" in task:
        return task, 400
    params = get_json_params(task)
    if "error" in params:
        return params, 400


    return "ok"

@tasker_bp.route("/")
def show_tasks():
    return "all the tasks"