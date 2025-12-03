from dataclasses import dataclass
from typing import Dict, Optional


@dataclass(slots=True, kw_only=True)
class HttpResponseValueObject:

    status_code: int
    message: Optional[str] = None
    body: Optional[Dict] = None
    