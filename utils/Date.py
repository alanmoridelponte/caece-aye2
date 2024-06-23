from datetime import datetime

def get_current_timestamp() -> str:
    return datetime.now().replace(microsecond=0).isoformat()