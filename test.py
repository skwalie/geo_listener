import json
from datetime import datetime

from repository import TraceCollection, Trace

if __name__ == "__main__":
    collection = TraceCollection(traces=[])

    try:
        with open(f"./out/positions-{datetime.today().strftime('%Y-%m-%d')}.json", "r", encoding="utf-8") as f:
            content = json.load(f)
            collection = TraceCollection(**content)

    except Exception as e:
        print("can't read positions from file")

    collection.traces.append(Trace(timestamp=1779094502, host="hom", lat=5.34,long=53.78))

    try:
        with open(f"./out/positions-{datetime.today().strftime('%Y-%m-%d')}.json", "w", encoding="utf-8") as f:
            f.write(collection.model_dump_json())
    except Exception as e:
        print("can't write positions to file")
