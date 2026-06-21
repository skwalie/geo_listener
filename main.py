
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, create_engine, select

from repository import Trace, create_db_and_tables, Traces

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
   # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = create_engine(url="postgresql://neondb_owner:npg_YH24WkdKUDul@ep-wandering-dream-alrifq4w.c-3.eu-central-1.aws.neon.tech/neondb?sslmode=require")

@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)

@app.get("/")
async def root():
    with Session(engine) as session:
        traces = session.exec(select(Traces)).all()

        return list(sorted(traces, key=lambda trace: trace.timestamp, reverse=True))

@app.post("/trace/")
async def trace_position(position: Trace, request: Request):
    try:
        traces = Traces(timestamp=position.timestamp, host=position.host, long=position.long, lat=position.lat)
        with Session(engine) as session:
            traces.ip = request.client.host.format()

            session.add(traces)
            session.commit()

    except Exception as e:
        print("can't read positions from file")
