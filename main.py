from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stations = [
    {
        "id": 1,
        "name": "МКС",
        "orbit": "Околоземная орбита",
        "crew": 7,
    },
    {
        "id": 2,
        "name": "Тяньгун",
        "orbit": "Околоземная орбита",
        "crew": 3,
    },
]


class StationCreate(BaseModel):
    name: str
    orbit: str
    crew: int


class Station(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int


@app.get("/stations", response_model=list[Station])
def get_stations():
    return stations


@app.post("/stations", response_model=Station, status_code=201)
def create_station(station: StationCreate):
    new_station = station.model_dump()
    new_station["id"] = len(stations) + 1
    stations.append(new_station)
    return new_station
