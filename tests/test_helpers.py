import pytest

from sanic_pydantic.helpers import serialize_query


@pytest.mark.parametrize('query, serialized_query', [
    ({}, {}),
    ({'param': [1]}, {'param': 1}),
    ({'param': [1, 2]}, {'param': 1}),
    ({'param_1': [1], 'param_2': [1, 2]}, {'param_1': 1, 'param_2': 1}),
])
def test_serialize_query(query, serialized_query):
    assert serialize_query(query) == serialized_query
