from dataclasses import dataclass, field


@dataclass(slots=True, kw_only=True)
class TokenValueObject:
    access_token: str | None = field(default=None) 
    refresh_token: str | None = field(default=None)
