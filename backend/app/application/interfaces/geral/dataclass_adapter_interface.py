from abc import ABC, abstractmethod
from typing import Any


class DataclassAdapterInterface(ABC):
    @abstractmethod
    def dataclass_to_dict(data: Any) -> dict:
        pass