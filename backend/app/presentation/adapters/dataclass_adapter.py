from dataclasses import asdict, is_dataclass
from typing import Any
from app.application.interfaces.geral.dataclass_adapter_interface import DataclassAdapterInterface


class DataclassAdapter(DataclassAdapterInterface):
    def dataclass_to_dict(self, data: Any) -> dict:

        if is_dataclass(data):
            return asdict(data)
        
        if isinstance(data, list):
            return [asdict(item) if is_dataclass(item) else item for item in data]
        
        return data
