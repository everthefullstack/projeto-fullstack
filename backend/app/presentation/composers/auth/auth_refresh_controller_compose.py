from app.infra.settings import settings
from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.infra.token.token_manager import TokenManager
from app.application.use_cases.auth.auth_refresh_use_case import AuthRefreshUseCase
from app.presentation.controllers.auth.auth_refresh_controller import AuthRefreshController


class AuthRefreshControllerComposer:

    @staticmethod
    def compose():
        
        dataclass_adapter = DataclassAdapter()
        token_manager = TokenManager(settings=settings, dataclass_adapter=dataclass_adapter)
        use_case = AuthRefreshUseCase(token_manager=token_manager)
        controller = AuthRefreshController(auth_refresh_use_case=use_case)

        return controller
