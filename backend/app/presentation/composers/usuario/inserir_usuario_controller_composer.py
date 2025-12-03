from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.infra.password.password_manager import PasswordManager
from app.infra.settings import settings
from app.infra.queue.redis_manager import RedisManager
from app.infra.repositories.redis_usuario_repository import RedisUsuarioRepository
from app.application.use_cases.usuario.inserir_usuario_use_case import InserirUsuarioUseCase
from app.presentation.controllers.usuario.inserir_usuario_controller import InserirUsuarioController


class InserirUsuarioControllerComposer:

    @staticmethod
    def compose():
        
        dataclass_adapter = DataclassAdapter()
        password = PasswordManager()
        redis = RedisManager(settings=settings).get_queue_client()
        repository = RedisUsuarioRepository(redis_client=redis, usuario_adapter=dataclass_adapter)
        use_case = InserirUsuarioUseCase(usuario_repository=repository, password_manager=password)
        controller = InserirUsuarioController(inserir_usuario_use_case=use_case)

        return controller
