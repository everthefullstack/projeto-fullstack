from abc import ABC, abstractmethod


class QueueManagerInterface(ABC):
    @abstractmethod
    def get_queue_client(self) -> None:
        pass
    