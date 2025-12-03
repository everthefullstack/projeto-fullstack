from abc import ABC, abstractmethod


class PasswordManagerInterface(ABC):
    @abstractmethod
    def hash(self, password: str) -> str:
        pass

    @abstractmethod
    def verify(self, password_hash: str, password: str) -> bool:
        pass
