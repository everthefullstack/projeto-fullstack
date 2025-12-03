from dataclasses import dataclass
from app.domain.erros.erros import ErroDeValueObject


@dataclass(slots=True, kw_only=True)
class AuthValueObject:
    login: str
    senha: str

    def validar_login(self) -> None:
        if not self.login:
            raise ErroDeValueObject("Dado de login não pode ser vazio.")
        
        return True
        
    def validar_senha(self) -> None:
        if not self.senha:
            raise ErroDeValueObject("Senha não pode ser vazia.")