from app.ext.api.models.audit_log import AuditLog
from app.ext.database import db


def create_audit(audit):
    audit_log = AuditLog()

    audit_log.action = audit.get("action")
    audit_log.object_type = audit.get("object_type")
    audit_log.object_id = audit.get("object_id")
    audit_log.object_name = audit.get("object_name")
    audit_log.done_by = audit.get("done_by")

    db.session.add(audit_log)
    db.session.commit()


def list_audit():
    logs = AuditLog.query.all()

    audit_list = [audit.as_dict() for audit in logs]

    return audit_list


def find_audit_by_id(audit_id):
    audit = AuditLog.query.filter_by(id=audit_id).first()

    return audit
