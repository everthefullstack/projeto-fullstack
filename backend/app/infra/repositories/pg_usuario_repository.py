from dataclasses import dataclass
from typing import Optional
from sqlalchemy.orm import Session
from app.domain.interfaces.usuario_repository_interface import UsuarioRepositoryInterface
from app.application.interfaces.geral.usuario_adapter_interface import UsuarioAdapterInterface
from app.domain.entities.usuario_entity import UsuarioEntity
from app.infra.models.sqlalchemy.usuario_model import UsuarioModel


@dataclass(slots=True, kw_only=True)
class PgUsuarioRepository(UsuarioRepositoryInterface):
    session: Optional[Session] = None
    usuario_adapter: UsuarioAdapterInterface

    def inserir_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        usuario_model: UsuarioModel = self.usuario_adapter.usuario_entity_to_usuario_model(data=usuario_entity)
        self.session.add(usuario_model)
        self.session.flush()

        return self.usuario_adapter.usuario_model_to_usuario_entity(data=usuario_model)
    
    def selecionar_usuario_por_id(self, usuario_id):
        usuario_model: UsuarioModel = self.session.query(UsuarioModel).filter(UsuarioModel.id == usuario_id).first()
        if usuario_model:
            return self.usuario_adapter.usuario_model_to_usuario_entity(data=usuario_model)
        
        return False

    def selecionar_usuario_por_email(self, usuario_email):
        usuario_model: UsuarioModel = self.session.query(UsuarioModel).filter(UsuarioModel.email == usuario_email).first()
        if usuario_model:
            return self.usuario_adapter.usuario_model_to_usuario_entity(data=usuario_model)
        
        return False
    
    def selecionar_usuario_por_username(self, usuario_username):
        usuario_model: UsuarioModel = self.session.query(UsuarioModel).filter(UsuarioModel.usuario == usuario_username).first()
        if usuario_model:
            return self.usuario_adapter.usuario_model_to_usuario_entity(data=usuario_model)
        
        return False
    
    def atualizar_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        usuario_model: UsuarioModel = self.usuario_adapter.usuario_entity_to_usuario_model(data=usuario_entity)
        self.session.add(usuario_model)
        self.session.flush()

        return self.usuario_adapter.usuario_model_to_usuario_entity(data=usuario_model)
    
    def deletar_usuario(self, usuario_id: str) -> None:
        usuario_model: UsuarioModel = self.session.get(UsuarioModel, usuario_id)
        if usuario_model:
            usuario_model.ativo = False
            self.session.add(usuario_model)
            self.session.flush()

            return True

        return False