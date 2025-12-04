from dataclasses import dataclass
from app.application.interfaces.produto.produto_use_case_interface import DeletarProdutoUseCaseInterface
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.domain.entities.produto_entity import ProdutoEntity
from app.presentation.adapters.dataclass_adapter import DataclassAdapter


@dataclass(slots=True, kw_only=True)
class DeletarProdutoController:

    deletar_produto_use_case: DeletarProdutoUseCaseInterface

    def deletar_produto(self, http_request_value_object: HttpRequestValueObject) -> HttpResponseValueObject:
        try:
            produto_id: str = http_request_value_object.path_params.get("id")

            produto_response = self.deletar_produto_use_case.deletar_produto(produto_id=produto_id)
            return HttpResponseValueObject(status_code=202, body=DataclassAdapter().dataclass_to_dict(data=produto_response))
    
        except Exception as e:
            return HttpResponseValueObject(status_code=500, body={"erro": str(e)})