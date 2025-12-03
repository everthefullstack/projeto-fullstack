from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.entities.usuario_entity import UsuarioEntity


class UsuarioRepositoryInterface(ABC):
    @abstractmethod
    def inserir_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        pass
    
    @abstractmethod
    def selecionar_usuario_por_id(self, usuario_id: int) -> Optional[UsuarioEntity]:
        pass
    
    @abstractmethod
    def selecionar_usuario_por_email(self, usuario_email: str) -> List[UsuarioEntity]: 
        pass
    
    @abstractmethod
    def selecionar_usuario_por_username(self, usuario_username: str) -> List[UsuarioEntity]: 
        pass

    @abstractmethod
    def atualizar_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        pass

    @abstractmethod
    def deletar_usuario(self, usuario_id: int) -> bool:
        pass    

class QueueUsuarioRepositoryInterface(ABC):
    @abstractmethod
    def inserir_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        pass

    @abstractmethod
    def atualizar_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        pass

    @abstractmethod
    def deletar_usuario(self, usuario_id: int) -> bool:
        pass