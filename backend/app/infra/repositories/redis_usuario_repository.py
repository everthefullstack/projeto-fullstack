import json
from typing import Optional
from dataclasses import dataclass
from redis import Redis
from app.domain.interfaces.usuario_repository_interface import QueueUsuarioRepositoryInterface
from app.application.interfaces.geral.dataclass_adapter_interface import DataclassAdapterInterface
from app.domain.entities.usuario_entity import UsuarioEntity


@dataclass(slots=True, kw_only=True) 
class RedisUsuarioRepository(QueueUsuarioRepositoryInterface):
    redis_client: Optional[Redis] = None
    usuario_adapter: DataclassAdapterInterface

    def inserir_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        usuario_dict = self.usuario_adapter.dataclass_to_dict(data=usuario_entity)
        message = {"action": "insert", "data": usuario_dict}
        self.redis_client.lpush("usuarios_queue", json.dumps(message, default=str))

        return {"status": "queued"}
    
    def atualizar_usuario(self, usuario_entity: UsuarioEntity) -> UsuarioEntity:
        usuario_dict = self.usuario_adapter.dataclass_to_dict(data=usuario_entity)
        message = {"action": "update", "data": usuario_dict}
        self.redis_client.lpush("usuarios_queue", json.dumps(message, default=str))

        return {"status": "queued"}
    
    def deletar_usuario(self, usuario_id: str) -> None:
        message = {"action": "delete", "data": usuario_id}
        self.redis_client.lpush("usuarios_queue", json.dumps(message, default=str))
        
        return {"status": "queued"}
        