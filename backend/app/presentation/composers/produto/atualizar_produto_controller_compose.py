from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.infra.settings import settings
from app.infra.queue.redis_manager import RedisManager
from app.infra.repositories.redis_produto_repository import RedisProdutoRepository
from app.application.use_cases.produto.atualizar_produto_use_case import AtualizarProdutoUseCase
from app.presentation.controllers.produto.atualizar_produto_controller import AtualizarProdutoController


class AtualizarProdutoControllerComposer:

    @staticmethod
    def compose():
        
        dataclass_adapter = DataclassAdapter()
        redis = RedisManager(settings=settings).get_queue_client()
        repository = RedisProdutoRepository(redis_client=redis, produto_adapter=dataclass_adapter)
        use_case = AtualizarProdutoUseCase(produto_repository=repository)
        controller = AtualizarProdutoController(atualizar_produto_use_case=use_case)

        return controller
