from dataclasses import dataclass
from app.application.interfaces.produto.produto_use_case_interface import InserirProdutoUseCaseInterface
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.domain.entities.produto_entity import ProdutoEntity
from app.presentation.adapters.dataclass_adapter import DataclassAdapter


@dataclass(slots=True, kw_only=True)
class InserirProdutoController:

    inserir_produto_use_case: InserirProdutoUseCaseInterface

    def inserir_produto(self, http_request_value_object: HttpRequestValueObject) -> HttpResponseValueObject:
        try:
            produto_entity: ProdutoEntity = ProdutoEntity(
                nome=http_request_value_object.body.get("nome"),
                marca=http_request_value_object.body.get("marca"),
                valor=http_request_value_object.body.get("valor"),
            )
            
            produto_response = self.inserir_produto_use_case.inserir_produto(produto_entity=produto_entity)
            return HttpResponseValueObject(status_code=202, body={"data": DataclassAdapter().dataclass_to_dict(data=produto_response)})
    
        except Exception as e:
            return HttpResponseValueObject(status_code=500, body={"erro": str(e)})