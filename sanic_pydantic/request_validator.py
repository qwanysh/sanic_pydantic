import asyncio
from functools import wraps
from typing import Callable, List, Optional

from pydantic import BaseModel, MissingError, ValidationError
from pydantic.error_wrappers import ErrorWrapper
from sanic import response

from .helpers import serialize_query, update_error_location


class RequestValidator:
    def __init__(
        self,
        query_object_name: str = 'query_',
        json_object_name: str = 'json_',
        status: int = 422,
    ):
        self._query_object_name = query_object_name
        self._json_object_name = json_object_name
        self._status = status

    def __call__(
        self,
        query_schema: BaseModel = None,
        json_schema: BaseModel = None,
        status: int = None,
    ):
        return self._get_decorator(
            query_schema, json_schema, status or self._status,
        )

    def _get_decorator(
        self,
        query_schema: Optional[BaseModel],
        json_schema: Optional[BaseModel],
        status: int,
    ):
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(request, *args, **kwargs):
                raw_errors = []

                if query_schema:
                    try:
                        kwargs[self._query_object_name] = query_schema(
                            **serialize_query(request.args),
                        )
                    except ValidationError as error:
                        raw_errors.extend(
                            update_error_location(
                                error, 'query',
                            ).raw_errors,
                        )

                if json_schema:
                    if request.json is not None:
                        try:
                            kwargs[self._json_object_name] = json_schema(
                                **request.json,
                            )
                        except ValidationError as error:
                            raw_errors.extend(
                                update_error_location(
                                    error, 'json',
                                ).raw_errors,
                            )
                    else:
                        error = ValidationError(
                            [ErrorWrapper(MissingError(), loc=('json',))],
                            json_schema,
                        )
                        raw_errors.extend(error.raw_errors)

                if raw_errors:
                    return self._get_error_response(raw_errors, status)

                return await self._get_response(func, request, *args, **kwargs)

            return wrapper

        return decorator

    def _get_error_response(self, raw_errors: List, status: int = None):
        error = ValidationError(raw_errors, BaseModel)
        return response.json(error.errors(), status=status)

    async def _get_response(self, func, request, *args, **kwargs):
        if asyncio.iscoroutinefunction(func):
            return await func(request, *args, **kwargs)

        return func(request, *args, **kwargs)
