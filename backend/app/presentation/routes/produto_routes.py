from flask import Blueprint, request, Response
from app.presentation.composers.produto.inserir_produto_controller_compose import InserirProdutoControllerComposer
from app.presentation.composers.produto.selecionar_produtos_controller_compose import SelecionarProdutosControllerComposer
from app.presentation.composers.produto.atualizar_produto_controller_compose import AtualizarProdutoControllerComposer
from app.presentation.composers.produto.deletar_produto_controller_compose import DeletarProdutoControllerComposer
from app.presentation.adapters.http_request_adapter import request_to_value_object
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.infra.schemas.http_response_schema import HttpResponseSchema
from app.infra.utils.authorizarion import authorization


produto_routes = Blueprint("produto", __name__, url_prefix="/api/v1/produto")

@produto_routes.route(rule="/", methods=["POST"])
@authorization
def inserir_produto():

    controller = InserirProdutoControllerComposer.compose()
    http_request: HttpRequestValueObject = request_to_value_object(request=request)
    http_response: HttpResponseValueObject = controller.inserir_produto(http_request_value_object=http_request)
    
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")

@produto_routes.route(rule="/", methods=["GET"])
@authorization
def selecionar_produtos():

    controller = SelecionarProdutosControllerComposer.compose()
    http_response: HttpResponseValueObject = controller.selecionar_produtos()
    
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")

@produto_routes.route(rule="/", methods=["PUT"])
@authorization
def atualizar_produto():
    controller = AtualizarProdutoControllerComposer.compose()
    http_request: HttpRequestValueObject = request_to_value_object(request=request)
    http_response: HttpResponseValueObject = controller.atualizar_produto(http_request_value_object=http_request)
    
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")

@produto_routes.route(rule="/<string:id>", methods=["DELETE"])
@authorization
def deletar_produto(id: str):
    controller = DeletarProdutoControllerComposer.compose()
    http_request: HttpRequestValueObject = request_to_value_object(request=request)
    http_response: HttpResponseValueObject = controller.deletar_produto(http_request_value_object=http_request)
    
    response = HttpResponseSchema(status_code=http_response.status_code,
                                  message=http_response.message,
                                  body=http_response.body)
    
    return Response(response=response.model_dump_json(exclude_none=True),
                    status=response.status_code,
                    mimetype="application/json")