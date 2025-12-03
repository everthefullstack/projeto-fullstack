from abc import ABC, abstractmethod


class SessionManagerInterface(ABC):
    @abstractmethod
    def get_session(self) -> None:
        pass

class EngineManagerInterface(ABC):
    @abstractmethod
    def get_engine(self) -> None:
        pass

class TableManagerInterface(ABC):
    @abstractmethod
    def create_table(self) -> None:
        pass