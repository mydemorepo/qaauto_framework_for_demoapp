import pytest
from modules.api.clients.my_client import MyClient
from modules.common import sqllitedb


@pytest.fixture
def client():
    client = MyClient('http://192.168.0.35:5000')
    yield client
    

@pytest.fixture
def database():
    database = sqllitedb.SqlliteDb("sampledatabase.sqlite")
    yield database
