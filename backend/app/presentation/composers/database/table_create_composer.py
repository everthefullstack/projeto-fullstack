from app.infra.database.sqlalchemy.table_manager import TableManager
from app.infra.database.sqlalchemy import engine
from app.infra.models.sqlalchemy.base_model import BaseModel
from typing import Any


class TableCreateComposer:

    @staticmethod
    def compose() -> Any:

        model = BaseModel()
        table = TableManager(engine=engine, model=model)
        
        return table