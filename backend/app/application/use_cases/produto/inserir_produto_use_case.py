from dataclasses import dataclass
from app.application.interfaces.produto.produto_use_case_interface import InserirProdutoUseCaseInterface
from app.domain.interfaces.produto_repository_interface import QueueProdutoRepositoryInterface
from app.domain.entities.produto_entity import ProdutoEntity
from app.domain.erros.erros import InserirProdutoErro


@dataclass(slots=True, kw_only=True)
class InserirProdutoUseCase(InserirProdutoUseCaseInterface):

    produto_repository: QueueProdutoRepositoryInterface

    def inserir_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        produto_entity.validar_nome()
        produto_entity.validar_marca()
        produto_entity.validar_valor()
        
        produto_response = self.produto_repository.inserir_produto(produto_entity=produto_entity)

        if produto_response:
            return produto_response
        
        raise InserirProdutoErro("Erro ao inserir produto.")