import pytest


@pytest.mark.test
def test_client(client):
    print(client.get_content('/api/json/offices'))
    assert 2/2 == 1

@pytest.mark.test    
def test_database (database):
    print(database.get_tables())
    assert 2/2 == 1