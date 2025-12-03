from dataclasses import dataclass, field
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from app.application.interfaces.geral.settings_manager_interface import SettingsManagerInterface
from app.application.interfaces.geral.database_manager_interface import EngineManagerInterface
from app.infra.utils.singleton import singleton


@singleton
@dataclass(slots=True, kw_only=True)
class EngineManager(EngineManagerInterface):
    
    __engine: Optional[Engine] = field(repr=False, init=False)
    __url: Optional[str] = field(repr=False, init=False)
    settings: SettingsManagerInterface

    def __create_engine(self) -> None:
        self.__url: str = self.settings.get_settings().DATABASE_URL
        self.__engine = create_engine(url=self.__url, echo=False)
        
    def __post_init__(self) -> None:
        self.__create_engine()

    def get_engine(self) -> None:
        return self.__engine
