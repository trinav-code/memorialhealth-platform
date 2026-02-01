from security.audit_logger import log_access

def get_patient(patient_id, user):
    log_access(user, "read", f"patient:{patient_id}")
    return {"id": patient_id, "status": "ok"}
