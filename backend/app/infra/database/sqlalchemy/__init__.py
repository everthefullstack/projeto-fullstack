from app.infra.database.sqlalchemy.engine_manager import EngineManager
from app.infra.settings import settings


engine = EngineManager(settings=settings)
