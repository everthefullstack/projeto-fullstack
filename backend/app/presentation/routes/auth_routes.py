from flask import Blueprint, request, Response
from app.presentation.composers.auth.auth_login_controller_compose import AuthLoginControllerComposer
from app.presentation.composers.auth.auth_refresh_controller_compose import AuthRefreshControllerComposer
from app.presentation.adapters.http_request_adapter import request_to_value_object
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.infra.schemas.http_response_schema import HttpResponseSchema
from app.infra.utils.authorizarion import refresh


auth_routes = Blueprint("auth", __name__, url_prefix="/api/v1/auth")

@auth_routes.route(rule="/login", methods=["POST"])
def login():

    controller = AuthLoginControllerComposer.compose()
    http_request: HttpRequestValueObject = request_to_value_object(request=request)
    http_response: HttpResponseValueObject = controller.login(http_request_value_object=http_request)
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")

@auth_routes.route(rule="/refresh", methods=["GET"])
@refresh
def refresh():

    controller = AuthRefreshControllerComposer.compose()
    http_request: HttpRequestValueObject = request_to_value_object(request=request)
    http_response: HttpResponseValueObject = controller.login(http_request_value_object=http_request)
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")