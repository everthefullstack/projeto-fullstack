from dataclasses import dataclass
from typing import List
from app.application.interfaces.produto.produto_use_case_interface import SelecionarProdutosUseCaseInterface
from app.application.interfaces.geral.unit_of_work_interface import UnitOfWorkInterface
from app.domain.entities.produto_entity import ProdutoEntity


@dataclass(slots=True, kw_only=True)
class SelecionarProdutosUseCase(SelecionarProdutosUseCaseInterface):

    unit_of_work: UnitOfWorkInterface

    def selecionar_produtos(self) -> List[ProdutoEntity]:
        with self.unit_of_work as uow:
            
            produto_response = uow.produto_repository.selecionar_produtos()

            if produto_response:
                return produto_response