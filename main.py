from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Каталог настольных игр",
    description="CRUD API для просмотра и управления каталогом настольных игр.",
    version="1.0.0",
)


class GameCreate(BaseModel):
    title: str = Field(min_length=1, description="Название игры")
    genre: str = Field(min_length=1, description="Жанр игры")
    players: int = Field(gt=0, description="Количество игроков")


class Game(GameCreate):
    id: int


games: list[Game] = [
    Game(id=1, title="Каркассон", genre="Стратегия", players=5),
    Game(id=2, title="Диксит", genre="Ассоциации", players=6),
]


@app.get("/games", response_model=list[Game])
def get_games():
    return games


@app.post("/games", response_model=Game, status_code=status.HTTP_201_CREATED)
def create_game(game: GameCreate):
    new_game = Game(id=max((item.id for item in games), default=0) + 1, **game.model_dump())
    games.append(new_game)
    return new_game


@app.put("/games/{game_id}", response_model=Game)
def update_game(game_id: int, game_update: GameCreate):
    for index, game in enumerate(games):
        if game.id == game_id:
            updated_game = Game(id=game_id, **game_update.model_dump())
            games[index] = updated_game
            return updated_game
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Игра не найдена")


@app.delete("/games/{game_id}", response_model=Game)
def delete_game(game_id: int):
    for index, game in enumerate(games):
        if game.id == game_id:
            return games.pop(index)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Игра не найдена")
