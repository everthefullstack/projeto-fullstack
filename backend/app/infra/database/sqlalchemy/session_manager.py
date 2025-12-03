from dataclasses import dataclass, field
from typing import Any, Optional
from sqlalchemy.orm import Session
from app.application.interfaces.geral.database_manager_interface import EngineManagerInterface
from app.application.interfaces.geral.database_manager_interface import SessionManagerInterface


@dataclass(slots=True, kw_only=True)
class SessionManager(SessionManagerInterface):
    
    __session: Optional[Session] = field(repr=False, init=False)
    engine: EngineManagerInterface

    def __create_session(self) -> None:
        self.__session = Session(self.engine.get_engine())
        
    def __post_init__(self) -> None:
        self.__create_session()

    def get_session(self) -> Any:
        return self.__session
    