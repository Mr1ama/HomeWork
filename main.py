from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class GameCreate(BaseModel):
    title: str
    genre: str
    players: int


class Game(BaseModel):
    id: int
    title: str
    genre: str
    players: int


games = [
    {
        "id": 1,
        "title": "Каркассон",
        "genre": "Стратегия",
        "players": 5,
    },
    {
        "id": 2,
        "title": "Диксит",
        "genre": "Ассоциации",
        "players": 6,
    },
]


@app.get("/games", response_model=list[Game])
def get_games():
    return games


@app.post("/games", response_model=Game, status_code=201)
def create_game(game: GameCreate):
    new_game = game.model_dump()
    new_game["id"] = len(games) + 1
    games.append(new_game)
    return new_game


@app.put("/games/{game_id}", response_model=Game)
def update_game(game_id: int, game: GameCreate):
    for index, saved_game in enumerate(games):
        if saved_game["id"] == game_id:
            updated_game = game.model_dump()
            updated_game["id"] = game_id
            games[index] = updated_game
            return updated_game
    raise HTTPException(status_code=404, detail="Игра не найдена")


@app.delete("/games/{game_id}", response_model=Game)
def delete_game(game_id: int):
    for index, saved_game in enumerate(games):
        if saved_game["id"] == game_id:
            deleted_game = games.pop(index)
            return deleted_game
    raise HTTPException(status_code=404, detail="Игра не найдена")
\n