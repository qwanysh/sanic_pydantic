import pytest
from pydantic import BaseModel
from sanic import Sanic, response

from sanic_pydantic import RequestValidator

validator = RequestValidator()


@pytest.fixture
def schema():
    class Schema(BaseModel):
        param: int

    return Schema


@pytest.fixture
def test_client(schema):
    app = Sanic('app')

    @app.get('/query')
    @validator(query_schema=schema)
    def endpoint_get(request, query_):
        return response.json(query_.dict())

    @app.get('/async-query')
    @validator(query_schema=schema)
    async def endpoint_async_get(request, query_):
        return response.json(query_.dict())

    @app.post('/json')
    @validator(json_schema=schema)
    def endpoint_post(request, json_):
        return response.json(json_.dict())

    return app.test_client
