from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.produto_entity import ProdutoEntity


class InserirProdutoUseCaseInterface(ABC):
    @abstractmethod
    def inserir_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        pass

class SelecionarProdutosUseCaseInterface(ABC):
    @abstractmethod
    def selecionar_produtos(self) -> List[ProdutoEntity]:
        pass

class AtualizarProdutoUseCaseInterface(ABC):
    @abstractmethod
    def atualizar_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        pass

class DeletarProdutoUseCaseInterface(ABC):
    @abstractmethod
    def deletar_produto(self, produto_id: str) -> None:
        pass