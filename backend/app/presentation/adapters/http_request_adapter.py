from flask import Request
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject


def request_to_value_object(request: Request) -> HttpRequestValueObject:
    return HttpRequestValueObject(
        body=request.json if request.method in ["POST", "PUT", "PATCH"] else None,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
    )