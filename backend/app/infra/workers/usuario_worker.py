from dataclasses import dataclass
import json
import time
from app.domain.entities.usuario_entity import UsuarioEntity
from app.application.interfaces.geral.unit_of_work_interface import UnitOfWorkInterface
from app.application.interfaces.geral.queue_manager_interface import QueueManagerInterface


@dataclass(slots=True, kw_only=True)
class UsuarioWorker:
    redis_client: QueueManagerInterface
    unit_of_work: UnitOfWorkInterface

    def run(self):
        while True:
            data = self.redis_client.brpop("usuarios_queue", timeout=5)
            if data:
                _, raw = data
                message = json.loads(raw)
                action = message["action"]
                payload = message["data"]

                if action == "insert":
                    usuario_entity = UsuarioEntity(**payload)
                    with self.unit_of_work as uow:
                        uow.usuario_repository.inserir_usuario(usuario_entity=usuario_entity)

                elif action == "update":
                    usuario_entity = UsuarioEntity(**payload)
                    with self.unit_of_work as uow:
                        uow.usuario_repository.atualizar_usuario(usuario_entity=usuario_entity)

                elif action == "delete":
                    with self.unit_of_work as uow:
                        uow.usuario_repository.deletar_usuario(usuario_id=payload["id"])
            else:
                time.sleep(1)