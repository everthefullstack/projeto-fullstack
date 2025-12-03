from dataclasses import dataclass
from app.application.interfaces.auth.auth_use_case_interface import AuthRefreshUseCaseInterface
from app.application.interfaces.geral.token_manager_interface import TokenManagerInterface
from app.domain.value_objects.token_value_object import TokenValueObject


@dataclass(slots=True, kw_only=True)
class AuthRefreshUseCase(AuthRefreshUseCaseInterface):
    token_manager: TokenManagerInterface

    def refresh(self, refresh_token: str) -> str:
        
        usuario_response = self.token_manager.decode_token(token=refresh_token)
        token_value_object = TokenValueObject(access_token=self.token_manager.create_access_token(data=usuario_response),
                                              refresh_token=refresh_token)
        
        return token_value_object
        
            