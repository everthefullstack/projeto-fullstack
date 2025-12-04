from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
import uuid

@dataclass(slots=True, kw_only=True)
class ProdutoEntity:
    id: Optional[uuid.UUID] = field(default=None)
    nome: str
    marca: str
    valor: float
    ativo: bool = field(default=True)
    criado_em: Optional[datetime] = field(default=None)
    atualizado_em: Optional[datetime] = field(default=None)

    def validar_nome(self) -> None:
        if not self.nome:
            raise ValueError("Nome do produto não pode ser vazio.")
        
        if not isinstance(self.nome, str):
            raise TypeError("Nome do produto deve ser uma string.")

    def validar_marca(self) -> None:
        if not self.marca:
            raise ValueError("Marca do produto não pode ser vazia.")
        
        if not isinstance(self.marca, str):
            raise TypeError("Marca do produto deve ser uma string.")

    def validar_valor(self) -> None:        
        if not isinstance(self.valor, float):
            try:
                self.valor = float(self.valor)
            except ValueError:
                raise TypeError("O valor do produto deve ser um número.")
            
        if self.valor <= 0:
            raise ValueError("O valor do produto deve ser maior que zero.")