from dataclasses import dataclass
import json
import time
from app.domain.entities.produto_entity import ProdutoEntity
from app.application.interfaces.geral.unit_of_work_interface import UnitOfWorkInterface
from app.application.interfaces.geral.queue_manager_interface import QueueManagerInterface


@dataclass(slots=True, kw_only=True)
class ProdutoWorker:
    redis_client: QueueManagerInterface
    unit_of_work: UnitOfWorkInterface

    def run(self):
        while True:
            data = self.redis_client.brpop("produtos_queue", timeout=5)
            if data:
                _, raw = data
                message = json.loads(raw)
                action = message["action"]
                payload = message["data"]

                if action == "insert":
                    produto_entity = ProdutoEntity(**payload)
                    with self.unit_of_work as uow:
                        uow.produto_repository.inserir_produto(produto_entity=produto_entity)

                elif action == "update":
                    produto_entity = ProdutoEntity(**payload)
                    with self.unit_of_work as uow:
                        uow.produto_repository.atualizar_produto(produto_entity=produto_entity)

                elif action == "delete":
                    with self.unit_of_work as uow:
                        uow.produto_repository.deletar_produto(produto_id=payload)
            else:
                time.sleep(1)