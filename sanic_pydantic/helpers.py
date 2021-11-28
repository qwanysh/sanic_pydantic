from pydantic import ValidationError
from pydantic.error_wrappers import ErrorList
from sanic.request import RequestParameters


def serialize_query(query: RequestParameters):
    return {key: values[0] for key, values in query.items()}


def update_error_location(error: ValidationError, location: str):
    for errors in error.raw_errors:
        if isinstance(errors, list):
            errors = [
                _update_raw_error_location(error, location)
                for error in errors
            ]
        else:
            errors = _update_raw_error_location(errors, location)

    return error


def _update_raw_error_location(errors: ErrorList, location: str):
    errors._loc = location, *errors.loc_tuple()
    return errors
