from app.ext.api.models.audit_log import AuditLog
from app.ext.database import db


def create_audit(action, object_id, object_name, object_type, done_by):
    audit_log = AuditLog()

    audit_log.action = action
    audit_log.object_id = object_id
    audit_log.object_name = object_name
    audit_log.done_by = done_by

    db.session.add(audit_log)
    db.session.commit()


def list_audit():
    logs = AuditLog.query.all()

    audit_list = [audit.as_dict() for audit in logs]

    return audit_list


def find_audit_by_id(audit_id):
    audit = AuditLog.query.filter_by(id=audit_id).first()

    return audit
