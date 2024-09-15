from flask import Blueprint

tasker_bp = Blueprint("tasker",__name__, url_prefix="/tasker")

@tasker_bp.route("/", methods=["POST"])
def do_task():
    return "do task"

@tasker_bp.route("/")
def show_tasks():
    return "all the tasks"