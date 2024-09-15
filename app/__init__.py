from flask import Flask
from .tasker.routes import tasker_bp
from .tasker.models import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tasker_bp)

    db_uri = "sqlite:///db.sqlite3"
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app