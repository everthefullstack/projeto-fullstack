from dataclasses import dataclass
from app.application.interfaces.auth.auth_use_case_interface import AuthLoginUseCaseInterface
from app.application.interfaces.geral.token_manager_interface import TokenManagerInterface
from app.application.interfaces.geral.unit_of_work_interface import UnitOfWorkInterface
from app.application.interfaces.geral.password_manager_interface import PasswordManagerInterface
from app.domain.erros.erros import CredenciaisInvalidasErro
from app.domain.value_objects.auth_value_object import AuthValueObject
from app.domain.value_objects.token_value_object import TokenValueObject


@dataclass(slots=True, kw_only=True)
class AuthLoginUseCase(AuthLoginUseCaseInterface):
    unit_of_work: UnitOfWorkInterface
    token_manager: TokenManagerInterface
    password_manager: PasswordManagerInterface

    def login(self, auth_value_object: AuthValueObject) -> str:
        with self.unit_of_work as uow:

            auth_value_object.validar_login()
            auth_value_object.validar_senha()

            usuario_response = None

            if auth_value_object.login.isalnum():
                usuario_response = uow.usuario_repository.selecionar_usuario_por_username(
                    auth_value_object.login
                )

            if "@" in auth_value_object.login and ".com" in auth_value_object.login:
                usuario_response = uow.usuario_repository.selecionar_usuario_por_email(
                    auth_value_object.login
                )

            if not usuario_response:
                raise CredenciaisInvalidasErro("Usuário ou senha inválidos.")

            if not self.password_manager.verify(usuario_response.senha, auth_value_object.senha):
                raise CredenciaisInvalidasErro("Usuário ou senha inválidos.")

            token_value_object = TokenValueObject(
                access_token=self.token_manager.create_access_token(data=usuario_response),
                refresh_token=self.token_manager.create_refresh_token(data=usuario_response)
            )
            
            return token_value_object

       
        