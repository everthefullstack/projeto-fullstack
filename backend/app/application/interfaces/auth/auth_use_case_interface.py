from abc import ABC, abstractmethod
from app.domain.value_objects.auth_value_object import AuthValueObject
from app.domain.value_objects.token_value_object import TokenValueObject


class AuthLoginUseCaseInterface(ABC):
    @abstractmethod
    def login(self, auth_value_object: AuthValueObject) -> TokenValueObject:
        pass

class AuthRefreshUseCaseInterface(ABC):
    @abstractmethod
    def refresh(self, refresh_token: str) -> TokenValueObject:
        pass