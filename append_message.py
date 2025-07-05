# append_message.py
import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data.json")

def save_message(msg: str):
    data = []
    if DATA_FILE.exists():
        data = json.loads(DATA_FILE.read_text())

    data.append({
        "text": msg,
        "time": datetime.now().isoformat()
    })

    DATA_FILE.write_text(json.dumps(data, indent=2))
