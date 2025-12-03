from abc import ABC, abstractmethod
from typing import Any


class UsuarioAdapterInterface(ABC):
    @abstractmethod
    def usuario_entity_to_usuario_model(data: Any) -> None:
        pass

    @abstractmethod
    def usuario_model_to_usuario_entity(data: Any) -> None:
        pass
    