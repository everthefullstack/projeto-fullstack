from dataclasses import dataclass, field
from typing import Optional
from redis import Redis
from app.application.interfaces.geral.queue_manager_interface import QueueManagerInterface
from app.application.interfaces.geral.settings_manager_interface import SettingsManagerInterface
from app.infra.utils.singleton import singleton


@singleton
@dataclass(slots=True, kw_only=True)
class RedisManager(QueueManagerInterface):

    __redis_client: Optional[Redis] = field(repr=False, init=False)
    settings: SettingsManagerInterface

    def __create_redis_client(self) -> None:
        self.__redis_client = Redis(
            host=self.settings.get_settings().REDIS_HOST,
            port=self.settings.get_settings().REDIS_PORT,
        )

    def __post_init__(self) -> None:
        self.__create_redis_client()

    def get_queue_client(self) -> Redis:
        return self.__redis_client
