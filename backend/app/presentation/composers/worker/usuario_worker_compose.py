from app.presentation.adapters.usuario_adapter import UsuarioAdapter
from app.infra.queue.redis_manager import RedisManager
from app.infra.settings import settings
from app.infra.database.sqlalchemy import engine
from app.infra.database.sqlalchemy.session_manager import SessionManager
from app.infra.repositories.pg_usuario_repository import PgUsuarioRepository
from app.infra.unit_of_work.usuario_unit_of_work import UsuarioUnitOfWork
from app.infra.workers.usuario_worker import UsuarioWorker
from typing import Any


class UsuarioWorkerComposer:

    @staticmethod
    def compose() -> Any:
        usuario_adapter = UsuarioAdapter()
        redis = RedisManager(settings=settings).get_queue_client()
        session = SessionManager(engine=engine).get_session()
        repository = PgUsuarioRepository(usuario_adapter=usuario_adapter)
        unit_of_work = UsuarioUnitOfWork(session=session, usuario_repository=repository)
        worker = UsuarioWorker(redis_client=redis, unit_of_work=unit_of_work)

        return worker
