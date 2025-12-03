from dataclasses import dataclass
from app.application.interfaces.usuario.usuario_use_case_interface import InserirUsuarioUseCaseInterface
from app.application.interfaces.geral.password_manager_interface import PasswordManagerInterface
from app.domain.interfaces.usuario_repository_interface import QueueUsuarioRepositoryInterface
from app.domain.entities.usuario_entity import UsuarioEntity


@dataclass(slots=True, kw_only=True)
class InserirUsuarioUseCase(InserirUsuarioUseCaseInterface):

    usuario_repository: QueueUsuarioRepositoryInterface
    password_manager: PasswordManagerInterface

    def inserir_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        usuario_entity.validar_usuario()
        usuario_entity.validar_email()
        usuario_entity.validar_senha()
        
        usuario_entity.senha = self.password_manager.hash(usuario_entity.senha)

        usuario_response = self.usuario_repository.inserir_usuario(usuario_entity=usuario_entity)

        if usuario_response:
            return usuario_response
