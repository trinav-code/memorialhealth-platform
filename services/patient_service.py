# WARNING: This PR adds new imports that may need to be verified:
#   from services.auth_service import check_permission
# Ensure these modules exist before merging
from security.audit_logger import log_access
from services.auth_service import check_permission

def get_patient(patient_id, user):
    if not check_permission(user, "read", f"patient:{patient_id}"):
        return {"status": "error", "message": "Unauthorized access"}
    log_access(user, "read", f"patient:{patient_id}")
    return {"id": patient_id, "status": "ok"}