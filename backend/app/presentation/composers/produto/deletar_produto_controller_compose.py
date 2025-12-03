from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.infra.settings import settings
from app.infra.queue.redis_manager import RedisManager
from app.infra.repositories.redis_produto_repository import RedisProdutoRepository
from app.application.use_cases.produto.deletar_produto_use_case import DeletarProdutoUseCase
from app.presentation.controllers.produto.deletar_produto_controller import DeletarProdutoController


class DeletarProdutoControllerComposer:

    @staticmethod
    def compose():
        
        dataclass_adapter = DataclassAdapter()
        redis = RedisManager(settings=settings).get_queue_client()
        repository = RedisProdutoRepository(redis_client=redis, produto_adapter=dataclass_adapter)
        use_case = DeletarProdutoUseCase(produto_repository=repository)
        controller = DeletarProdutoController(deletar_produto_use_case=use_case)

        return controller
