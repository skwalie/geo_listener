import json
from datetime import datetime

from fastapi import FastAPI, Request

from repository import Trace, TraceCollection

app = FastAPI()



@app.get("/")
async def root():
    pass

@app.post("/trace/")
async def trace_position(position: Trace, request: Request):
    collection = TraceCollection(traces=[])

    try:
        with open(f"./out/positions-{datetime.today().strftime('%Y-%m-%d')}.json", "r", encoding="utf-8") as f:
            content = json.load(f)
            collection = TraceCollection(**content)

    except Exception as e:
        print("can't read positions from file")

    position.ip = request.client.host.format()
    collection.traces.append(position)

    try:
        with open(f"./out/positions-{datetime.today().strftime('%Y-%m-%d')}.json", "w", encoding="utf-8") as f:
            f.write(collection.model_dump_json())
    except Exception as e:
        print("can't write positions to file")


