from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from typing import Dict


def value_object_to_response(status_code: int, message: str, data: Dict) -> HttpResponseValueObject:

    return HttpResponseValueObject(
        status_code=status_code,
        message=message,
        body=data
    )
