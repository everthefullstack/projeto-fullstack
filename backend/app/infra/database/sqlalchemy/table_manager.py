from dataclasses import dataclass
from app.application.interfaces.geral.database_manager_interface import TableManagerInterface, EngineManagerInterface
from app.infra.models.sqlalchemy.base_model import BaseModel


@dataclass(slots=True, kw_only=True)
class TableManager(TableManagerInterface):
    
    engine: EngineManagerInterface
    model: BaseModel

    def create_table(self) -> None:
        try:
            self.model.metadata.create_all(self.engine.get_engine())
        
        except Exception as e:
            raise e
        