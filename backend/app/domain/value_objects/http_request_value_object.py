from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(slots=True, kw_only=True)
class HttpRequestValueObject:

    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, str]] = None
    query_params: Optional[Dict[str, str]] = None
    path_params: Optional[Dict[str, str]] = None
    url: Optional[str] = None
    ipv4: Optional[str] = None
    