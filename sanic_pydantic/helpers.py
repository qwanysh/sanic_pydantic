from pydantic import ValidationError
from sanic.request import RequestParameters


def serialize_query(query: RequestParameters):
    return {key: values[0] for key, values in query.items()}


def get_error_with_updated_location(error: ValidationError, location: str):
    for raw_error in error.raw_errors:
        raw_error._loc = location, *raw_error.loc_tuple()

    return error
