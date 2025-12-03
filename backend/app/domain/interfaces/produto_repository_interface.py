from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.produto_entity import ProdutoEntity


class ProdutoRepositoryInterface(ABC):
    @abstractmethod
    def inserir_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        pass

    @abstractmethod
    def selecionar_produtos(self) -> List[ProdutoEntity]:
        pass

    @abstractmethod
    def selecionar_produto_por_id(self, produto_id: str) -> ProdutoEntity:
        pass

    @abstractmethod
    def atualizar_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        pass

    @abstractmethod
    def deletar_produto(self, produto_id: int) -> bool:
        pass

class QueueProdutoRepositoryInterface(ABC):
    @abstractmethod
    def inserir_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        pass

    @abstractmethod
    def atualizar_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        pass

    @abstractmethod
    def deletar_produto(self, produto_id: int) -> bool:
        pass