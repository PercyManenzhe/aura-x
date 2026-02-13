import os
import json
from datetime import datetime

def save_run_local(result: dict, folder: str = "runs") -> str:
    os.makedirs(folder, exist_ok=True)

    run_id = result.get("run_id", "AX-UNKNOWN")
    workflow = result.get("workflow", "unknown")
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"{folder}/{workflow}_{run_id}_{ts}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    return filename
