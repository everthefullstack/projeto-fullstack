import jwt
from dataclasses import dataclass
from typing import Any
from datetime import datetime, timedelta, timezone
from app.application.interfaces.geral.token_manager_interface import TokenManagerInterface
from app.application.interfaces.geral.settings_manager_interface import SettingsManagerInterface
from app.application.interfaces.geral.dataclass_adapter_interface import DataclassAdapterInterface


@dataclass(slots=True, kw_only=True)
class TokenManager(TokenManagerInterface):

    settings: SettingsManagerInterface
    dataclass_adapter: DataclassAdapterInterface
    
    def create_access_token(self, data: Any) -> str:
        to_encode = self.dataclass_adapter.dataclass_to_dict(data=data)

        expire = (datetime.now(timezone.utc) + 
                  timedelta(minutes=self.settings.get_settings().ACCESS_TOKEN_EXPIRE_MINUTES))
        
        to_encode.update({"exp": expire})

        token = jwt.encode(payload=to_encode, 
                           key=self.settings.get_settings().SECRET_KEY, 
                           algorithm=self.settings.get_settings().ALGORITHM)
        return token

    def create_refresh_token(self, data: Any) -> str:
        to_encode = self.dataclass_adapter.dataclass_to_dict(data=data)

        expire = (datetime.now(timezone.utc) + 
                  timedelta(days=self.settings.get_settings().REFRESH_TOKEN_EXPIRE_DAYS))
        
        to_encode.update({"exp": expire})
        
        token = jwt.encode(payload=to_encode, 
                           key=self.settings.get_settings().SECRET_KEY, 
                           algorithm=self.settings.get_settings().ALGORITHM)
        return token
    
    def decode_token(self, token: str) -> dict:
        decoded_token = jwt.decode(token, 
                                   self.settings.get_settings().SECRET_KEY, 
                                   algorithms=[self.settings.get_settings().ALGORITHM])
        return decoded_token
