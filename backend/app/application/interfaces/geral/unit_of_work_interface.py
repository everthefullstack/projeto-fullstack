from abc import ABC, abstractmethod


class UnitOfWorkInterface(ABC):

    @abstractmethod
    def __enter__(self) -> "UnitOfWorkInterface":
        pass
    
    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
