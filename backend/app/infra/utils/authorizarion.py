import jwt
from functools import wraps
from flask import request, Response
from app.infra.settings import settings
from app.infra.schemas.http_response_schema import HttpResponseSchema
from app.presentation.composers.token.token_manager_compose import TokenManagerComposer


token_manager = TokenManagerComposer.compose()

def authorization(func):
    @wraps(func)
    def authorize(*args, **kwargs):

        access_token = request.headers.get("Authorization", None)

        if not access_token:
            response = HttpResponseSchema(status_code=403, body={"data": "Token de autorização não fornecido."})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")
        
        try:
            access_token = str(request.headers["Authorization"]).replace("Bearer ", "")
            jwt.decode(access_token, settings.get_settings().SECRET_KEY, algorithms=settings.get_settings().ALGORITHM)
            return func(*args, **kwargs)
        
        except jwt.ExpiredSignatureError:
            response = HttpResponseSchema(status_code=401, body={"data": "Access token expirado"})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")
        
        except jwt.InvalidTokenError:
            response = HttpResponseSchema(status_code=401, body={"data": "Token inválido."})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")

        except Exception as e:
            response = HttpResponseSchema(status_code=500, body={"data": f"Erro interno no servidor: {str(e)}"})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")

    return authorize


def refresh(func):
    @wraps(func)
    def refresher(*args, **kwargs):

        refresh_token = request.headers.get("Authorization", None)

        if not refresh_token:
            response = HttpResponseSchema(status_code=403, body={"data": "Token de refresh não fornecido."})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")
        
        try:
            refresh_token = str(request.headers["Authorization"]).replace("Bearer ", "")
            jwt.decode(refresh_token, settings.get_settings().SECRET_KEY, algorithms=settings.get_settings().ALGORITHM)
            return func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            response = HttpResponseSchema(status_code=401, body={"data": "Refresh token expirado"})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")
        
        except jwt.InvalidTokenError:
            response = HttpResponseSchema(status_code=401, body={"data": "Token inválido."})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")

        except Exception as e:
            response = HttpResponseSchema(status_code=500, body={"data": f"Erro interno no servidor: {str(e)}"})
            return Response(response=response.model_dump_json(exclude_none=True), status=response.status_code, mimetype="application/json")
        
    return refresher
