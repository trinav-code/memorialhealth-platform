import logging

logger = logging.getLogger("audit")
logger.setLevel(logging.INFO)

def log_access(user, action, resource):
    logger.info(f"{user} {action} {resource}")
