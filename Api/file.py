from fastapi import FastAPI
import uvicorn
from Api.models import Games
from typing import Optional
import httpx

app=FastAPI()
spis_games=[]

@app.get('/')
def first_page():
    return {"message" : "Hello"}

@app.post("/create_game")
def post_create_game(game: Games):
    spis_games.append(game)
    return game

@app.get("/get_games")
def get_games():
    return spis_games

@app.get("/get_game")
def get_game(id:int):
    return spis_games[id]

@app.put("/put_game")
def put_game(id: int, game:Games):
    spis_games[id].numb=game.numb
    spis_games[id].name=game.name
    spis_games[id].price = game.price
    spis_games[id].descr = game.descr
    return spis_games[id]

@app.delete("/del")
def del_game(id:int):
    spis_games.pop(id)
    return spis_games

if __name__=="__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)