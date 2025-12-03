from dataclasses import dataclass
from app.application.interfaces.produto.produto_use_case_interface import DeletarProdutoUseCaseInterface
from app.domain.interfaces.produto_repository_interface import QueueProdutoRepositoryInterface
from app.domain.erros.erros import DeletarProdutoErro


@dataclass(slots=True, kw_only=True)
class DeletarProdutoUseCase(DeletarProdutoUseCaseInterface):

    produto_repository: QueueProdutoRepositoryInterface

    def deletar_produto(self, produto_id: int) -> bool:
            
        produto_response = self.produto_repository.deletar_produto(produto_id=produto_id)

        if produto_response:
            return produto_response
        
        raise DeletarProdutoErro("Erro ao deletar produto.")