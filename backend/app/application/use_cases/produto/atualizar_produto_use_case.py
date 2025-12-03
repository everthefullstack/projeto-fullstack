from dataclasses import dataclass
from app.application.interfaces.produto.produto_use_case_interface import AtualizarProdutoUseCaseInterface
from app.domain.interfaces.produto_repository_interface import QueueProdutoRepositoryInterface
from app.domain.entities.produto_entity import ProdutoEntity
from app.domain.erros.erros import AtualizarProdutoErro
from datetime import datetime, timezone


@dataclass(slots=True, kw_only=True)
class AtualizarProdutoUseCase(AtualizarProdutoUseCaseInterface):

    produto_repository: QueueProdutoRepositoryInterface

    def atualizar_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        produto_entity.validar_nome()
        produto_entity.validar_marca()
        produto_entity.validar_valor()
        produto_entity.atualizado_em = datetime.now(timezone.utc)
        produto_response = self.produto_repository.atualizar_produto(produto_entity=produto_entity)

        if produto_response:
            return produto_response
        
        raise AtualizarProdutoErro("Erro ao atualizar produto.")