from abc import ABC, abstractmethod
from app.domain.entities.usuario_entity import UsuarioEntity


class InserirUsuarioUseCaseInterface(ABC):
    @abstractmethod
    def inserir_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        pass

class SelecionarUsuarioPorIdUseCaseInterface(ABC):
    @abstractmethod
    def selecionar_usuario_por_id(self, usuario_id: int) -> UsuarioEntity:
        pass

class SelecionarUsuarioPorEmailUseCaseInterface(ABC):
    @abstractmethod
    def selecionar_usuario_por_email(self, usuario_email: str) -> UsuarioEntity:
        pass

class SelecionarUsuarioPorUsernameUseCaseInterface(ABC):
    @abstractmethod
    def selecionar_usuario_por_username(self, usuario_username: str) -> UsuarioEntity:
        pass
    
class AtualizarUsuarioUseCaseInterface(ABC):
    @abstractmethod
    def atualizar_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        pass

class DeletarUsuarioUseCaseInterface(ABC):
    @abstractmethod
    def deletar_usuario(self, usuario_id: int) -> None:
        pass