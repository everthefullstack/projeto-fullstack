from app.presentation.adapters.usuario_adapter import UsuarioAdapter
from app.infra.settings import settings
from app.infra.database.sqlalchemy import engine
from app.infra.database.sqlalchemy.session_manager import SessionManager
from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.infra.token.token_manager import TokenManager
from app.infra.password.password_manager import PasswordManager
from app.infra.repositories.pg_usuario_repository import PgUsuarioRepository
from app.infra.unit_of_work.usuario_unit_of_work import UsuarioUnitOfWork
from app.application.use_cases.auth.auth_login_use_case import AuthLoginUseCase
from app.presentation.controllers.auth.auth_login_controller import AuthLoginController


class AuthLoginControllerComposer:

    @staticmethod
    def compose():
        
        password_manager = PasswordManager()
        usuario_adapter = UsuarioAdapter()
        dataclass_adapter = DataclassAdapter()
        session = SessionManager(engine=engine).get_session()
        token_manager = TokenManager(settings=settings, dataclass_adapter=dataclass_adapter)
        repository = PgUsuarioRepository(usuario_adapter=usuario_adapter)
        unit_of_work = UsuarioUnitOfWork(session=session, usuario_repository=repository)
        use_case = AuthLoginUseCase(unit_of_work=unit_of_work, token_manager=token_manager, password_manager=password_manager)
        controller = AuthLoginController(auth_login_use_case=use_case)

        return controller
