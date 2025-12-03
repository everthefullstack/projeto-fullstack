from dataclasses import dataclass
from app.application.interfaces.produto.produto_use_case_interface import SelecionarProdutosUseCaseInterface
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.presentation.adapters.dataclass_adapter import DataclassAdapter


@dataclass(slots=True, kw_only=True)
class SelecionarProdutosController:

    selecionar_produtos_use_case: SelecionarProdutosUseCaseInterface

    def selecionar_produtos(self) -> HttpResponseValueObject:
        try:
            produto_response = self.selecionar_produtos_use_case.selecionar_produtos()
            return HttpResponseValueObject(status_code=200, body={"data": DataclassAdapter().dataclass_to_dict(data=produto_response)})
    
        except Exception as e:
            return HttpResponseValueObject(status_code=500, body={"erro": str(e)})