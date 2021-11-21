from json import dumps
from urllib.parse import urlencode


def test_query_error(test_client):
    _, response = test_client.get('/query')
    assert response.status == 422


def test_query(test_client):
    query = {'param': 1}
    _, response = test_client.get(f'/query?{urlencode(query)}')
    assert response.status == 200
    assert response.json == query


def test_query_async(test_client):
    query = {'param': 1}
    _, response = test_client.get(f'/async-query?{urlencode(query)}')
    assert response.status == 200
    assert response.json == query


def test_json_empty(test_client):
    _, response = test_client.post('/json')
    assert response.status == 422
    assert response.json[0]['loc'] == ['json']


def test_json_error(test_client):
    data = {}
    _, response = test_client.post('/json', data=dumps(data))
    assert response.status == 422


def test_json(test_client):
    data = {'param': 1}
    _, response = test_client.post('/json', data=dumps(data))
    assert response.status == 200
    assert response.json == data
