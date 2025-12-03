from app.application.interfaces.geral.usuario_adapter_interface import UsuarioAdapterInterface
from app.domain.entities.usuario_entity import UsuarioEntity
from app.infra.models.sqlalchemy.usuario_model import UsuarioModel


class UsuarioAdapter(UsuarioAdapterInterface):
    @staticmethod
    def usuario_entity_to_usuario_model(data: UsuarioEntity) -> UsuarioModel:
        return UsuarioModel(usuario=data.usuario, 
                            senha=data.senha, 
                            email=data.email)
    
    @staticmethod
    def usuario_model_to_usuario_entity(data: UsuarioModel) -> UsuarioEntity:
        return UsuarioEntity(id=str(data.id),
                             usuario=data.usuario, 
                             senha=data.senha, 
                             email=data.email)
