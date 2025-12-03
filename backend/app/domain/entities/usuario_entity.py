from dataclasses import dataclass, field
from typing import Optional
from app.domain.erros.erros import ErroDeDominio
import uuid


@dataclass(slots=True, kw_only=True)
class UsuarioEntity:
    id: Optional[uuid.UUID] = field(default=None)
    usuario: str
    email: str
    senha: str
    ativo: bool = field(default=True)

    def validar_usuario(self) -> None:
        if not self.usuario:
            raise ErroDeDominio("Usuário não pode ser vazio.")
        
        if not self.usuario.isalnum():
            raise ErroDeDominio("Usuário deve conter apenas caracteres alfanuméricos(A-Z, 0-9).")
        
        if len(self.usuario) < 2 or len(self.usuario) > 20:
            raise ErroDeDominio("Usuário deve ter entre 2 e 20 caracteres.")
    
    def validar_email(self) -> None:
        if not self.email:
            raise ErroDeDominio("Email não pode ser vazio.")
        
        if type(self.email) is not str:
            raise ErroDeDominio("Email deve ser uma string.")
        
        if "@" not in self.email or "." not in self.email:
            raise ErroDeDominio("Email inválido.")

    def validar_senha(self) -> None:
        if not self.senha:
            raise ErroDeDominio("Senha não pode ser vazia.")
        
        if type(self.senha) is not str:
            raise ErroDeDominio("Senha deve ser uma string.")
        
        if len(self.senha) < 6:
            raise ErroDeDominio("Senha deve ter no mínimo 6 caracteres.")
    