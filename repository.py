from pydantic import BaseModel


from sqlmodel import Field, SQLModel


class Trace(BaseModel):
    timestamp: int
    host: str
    long: float
    lat: float
    ip: str | None = None


class Traces(SQLModel, table=True):
    timestamp: int | None = Field(default=None, primary_key=True)
    host: str
    long: float
    lat: float
    ip: str | None = None


def create_db_and_tables(engine):
    SQLModel.metadata.create_all(engine)

