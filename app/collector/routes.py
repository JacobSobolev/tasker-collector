from flask import Blueprint, request

collector_bp = Blueprint("collector",__name__, url_prefix="/collector")

collector_bp.route("/", methods=['POST'])
def collector_job():
    return "doing collector job"