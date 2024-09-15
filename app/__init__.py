from flask import Flask
from .tasker.routes import tasker_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(tasker_bp)

    return app