from abc import ABC, abstractmethod


class SettingsManagerInterface(ABC):
    @abstractmethod
    def get_settings(self) -> None:
        pass
    