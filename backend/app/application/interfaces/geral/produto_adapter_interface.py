from abc import ABC, abstractmethod
from typing import Any


class ProdutoAdapterInterface(ABC):
    @abstractmethod
    def produto_entity_to_produto_model(data: Any) -> None:
        pass

    @abstractmethod
    def produto_model_to_produto_entity(data: Any) -> None:
        pass
    