import os
import json
from datetime import datetime


class StorageAdapter:

    def __init__(self, base_folder: str = "runs"):
        self.base_folder = base_folder
        os.makedirs(self.base_folder, exist_ok=True)

    # =====================================================
    # SAVE RUN
    # =====================================================
    def save_run(self, result: dict) -> str:

        run_id = result.get("run_id", "AX-UNKNOWN")
        workflow = result.get("workflow", "unknown")
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

        filename = f"{workflow}_{run_id}_{timestamp}.json"
        path = os.path.join(self.base_folder, filename)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return path

    # =====================================================
    # LOAD RUN
    # =====================================================
    def load_run(self, filename: str):

        path = os.path.join(self.base_folder, filename)

        if not os.path.exists(path):
            return {
                "status": "error",
                "message": "File not found"
            }

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    # =====================================================
    # LIST RUNS
    # =====================================================
    def list_runs(self):

        files = os.listdir(self.base_folder)

        return [
            {
                "file": f,
                "path": os.path.join(self.base_folder, f)
            }
            for f in files if f.endswith(".json")
        ]

    # =====================================================
    # DELETE RUN
    # =====================================================
    def delete_run(self, filename: str):

        path = os.path.join(self.base_folder, filename)

        if os.path.exists(path):
            os.remove(path)
            return {"status": "deleted", "file": filename}

        return {"status": "error", "message": "File not found"}
