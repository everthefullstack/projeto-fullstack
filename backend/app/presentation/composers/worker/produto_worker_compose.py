from app.presentation.adapters.produto_adapter import ProdutoAdapter
from app.infra.queue.redis_manager import RedisManager
from app.infra.settings import settings
from app.infra.database.sqlalchemy import engine
from app.infra.database.sqlalchemy.session_manager import SessionManager
from app.infra.repositories.pg_produto_repository import PgProdutoRepository
from app.infra.unit_of_work.produto_unit_of_work import ProdutoUnitOfWork
from app.infra.workers.produto_worker import ProdutoWorker
from typing import Any


class ProdutoWorkerComposer:
    @staticmethod
    def compose() -> Any:
        produto_adapter = ProdutoAdapter()
        redis = RedisManager(settings=settings).get_queue_client()
        session = SessionManager(engine=engine).get_session()
        repository = PgProdutoRepository(produto_adapter=produto_adapter)
        unit_of_work = ProdutoUnitOfWork(session=session, produto_repository=repository)
        worker = ProdutoWorker(redis_client=redis, unit_of_work=unit_of_work)

        return worker
