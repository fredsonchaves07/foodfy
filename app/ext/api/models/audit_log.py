from datetime import datetime
from uuid import uuid4

from app.ext.database import db


class AuditLog(db.Model):
    __tablename__ = "audit_log"

    id = db.Column("id", db.String(), primary_key=True, autoincrement=False)
    action = db.Column("action", db.String())
    object_id = db.Column("object_id", db.String())
    object_name = db.Column("object_name", db.String())
    object_type = db.Column("object_type", db.String())
    done_by = db.Column("done_by", db.String())
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())

    def __init__(self):
        self.id = str(uuid4())

    def as_dict(self):
        return {
            "id": str(self.id),
            "action": self.action,
            "object_id": self.object_id,
            "object_name": self.object_name,
            "object_type": self.object_type,
            "done_by": self.done_by,
            "created_date": self.created_date,
        }
