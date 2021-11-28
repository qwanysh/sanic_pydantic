import pytest
from pydantic import BaseModel, ValidationError
from pydantic.error_wrappers import ErrorWrapper

from sanic_pydantic.helpers import (_update_raw_error_location,
                                    serialize_query, update_error_location)


@pytest.mark.parametrize('query, serialized_query', [
    ({}, {}),
    ({'param': [1]}, {'param': 1}),
    ({'param': [1, 2]}, {'param': 1}),
    ({'param_1': [1], 'param_2': [1, 2]}, {'param_1': 1, 'param_2': 1}),
])
def test_serialize_query(query, serialized_query):
    assert serialize_query(query) == serialized_query


def test_update_error_location():
    errors = ErrorWrapper(Exception(), loc=())
    error = ValidationError([errors], BaseModel)
    updated_error = update_error_location(error, 'new_location')
    assert updated_error.raw_errors[0].loc_tuple() == ('new_location',)


def test__update_raw_error_location():
    errors = ErrorWrapper(Exception(), loc=())
    updated_error = _update_raw_error_location(errors, 'new_location')
    assert updated_error.loc_tuple() == ('new_location',)
