from flask_sqlalchemy import SQLAlchemy
import uuid

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())


class Tasker(db.Model):
    uuid = db.Column(db.String, primary_key=True, default=generate_uuid)
    task = db.Column(db.String)
    params = db.Column(db.String)
    result = db.Column(db.String)
    req_ip = db.Column(db.String)
    time_stamp = db.Column(db.String)

    def get_dict(self):
        return {
            "uuid": self.uuid,
            "task": self.task,
            "params": self.params,
            "result": self.result,
            "req_ip": self.req_ip,
            "time_stamp": self.time_stamp
        }