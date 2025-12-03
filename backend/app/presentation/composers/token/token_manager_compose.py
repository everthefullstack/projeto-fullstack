from app.infra.settings import settings
from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.infra.token.token_manager import TokenManager


class TokenManagerComposer:

    @staticmethod
    def compose():
        
        dataclass_adapter = DataclassAdapter()
        token_manager = TokenManager(settings=settings, dataclass_adapter=dataclass_adapter)

        return token_manager
