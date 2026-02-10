from security.audit_logger import log_access
from security.access_control import has_permission

def get_patient(patient_id, user):
    if has_permission(user, "read", f"patient:{patient_id}"):
        log_access(user, "read", f"patient:{patient_id}")
        return {"id": patient_id, "status": "ok"}
    else:
        return {"status": "error", "message": "Access denied"}