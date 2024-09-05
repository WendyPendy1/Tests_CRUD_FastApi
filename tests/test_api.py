import pytest
from Api.file import app
from Api.models import Games
from faker import Faker
from fastapi.testclient import TestClient

client=TestClient(app=app)
fake=Faker()

@pytest.fixture(scope="function")
def post_game():
    payload={
        "numb": fake.random_int(),
        "name": fake.name(),
        "price": fake.random_int(),
        "descr": fake.text(max_nb_chars=10)
    }
    resp=client.post(url="/create_game", json=payload)
    return resp

@pytest.fixture(scope="function")
def get_games():
    resp=client.get(url="/get_games")
    return resp

def prov_isistance(get_games):
    resp_json = get_games.json()
    for item in resp_json:
        obj = Games(**item)
        assert isinstance(obj.name, str)
        assert isinstance(obj.numb, int)
        assert isinstance(obj.descr, str)
        assert isinstance(obj.price, int)

class TestCase:
    def test_post(self, post_game):
        assert post_game.status_code==200

    def test_get_games(self, get_games):
        assert get_games.status_code==200
        prov_isistance(get_games)




