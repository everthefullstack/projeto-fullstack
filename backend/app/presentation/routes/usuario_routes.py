from flask import Blueprint, request, Response
from app.presentation.composers.usuario.inserir_usuario_controller_composer import InserirUsuarioControllerComposer
from app.presentation.adapters.http_request_adapter import request_to_value_object
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.infra.schemas.http_response_schema import HttpResponseSchema


usuario_routes = Blueprint("usuario", __name__, url_prefix="/api/v1/usuario")

@usuario_routes.route(rule="/", methods=["POST"])
def inserir_usuario():

    controller = InserirUsuarioControllerComposer.compose()
    http_request: HttpRequestValueObject = request_to_value_object(request=request)
    http_response: HttpResponseValueObject = controller.inserir_usuario(http_request_value_object=http_request)
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")