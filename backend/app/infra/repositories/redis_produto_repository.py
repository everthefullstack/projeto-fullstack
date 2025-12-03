import json
from typing import Optional
from dataclasses import dataclass
from redis import Redis
from app.domain.interfaces.produto_repository_interface import QueueProdutoRepositoryInterface
from app.application.interfaces.geral.dataclass_adapter_interface import DataclassAdapterInterface
from app.domain.entities.produto_entity import ProdutoEntity


@dataclass(slots=True, kw_only=True) 
class RedisProdutoRepository(QueueProdutoRepositoryInterface):
    redis_client: Optional[Redis] = None
    produto_adapter: DataclassAdapterInterface

    def inserir_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        produto_dict = self.produto_adapter.dataclass_to_dict(data=produto_entity)
        message = {"action": "insert", "data": produto_dict}
        self.redis_client.lpush("produtos_queue", json.dumps(message, default=str))

        return True
    
    def atualizar_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        produto_dict = self.produto_adapter.dataclass_to_dict(data=produto_entity)
        message = {"action": "update", "data": produto_dict}
        self.redis_client.lpush("produtos_queue", json.dumps(message, default=str))

        return True
    
    def deletar_produto(self, produto_id: str) -> None:
        message = {"action": "delete", "data": produto_id}
        self.redis_client.lpush("produtos_queue", json.dumps(message, default=str))
        
        return True
        