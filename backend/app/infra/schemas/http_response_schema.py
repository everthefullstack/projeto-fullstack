from pydantic import BaseModel


class HttpResponseSchema(BaseModel):
    status_code: int
    message: str | None = None
    body: dict | list | None = None