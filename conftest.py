import pytest
from modules.api.clients.my_client import MyClient
from modules.common import sqllitedb
from modules.common import mysqldb

@pytest.fixture
def client():
    client = MyClient('http://192.168.0.72:5000')
    yield client
    

@pytest.fixture
def database():
    #database = mysqldb.MysqlDb("localhost", "root", "root", "classicmodels",)
    database = sqllitedb.SqlliteDb("sampledatabase.sqlite")
    yield database