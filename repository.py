from pydantic import BaseModel


class Trace(BaseModel):
    timestamp: int
    host: str
    long: float
    lat: float
    ip: str

class TraceCollection(BaseModel):
    traces: list[Trace]