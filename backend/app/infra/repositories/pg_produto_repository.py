from dataclasses import dataclass
from typing import Optional, List
from sqlalchemy.orm import Session
from app.domain.interfaces.produto_repository_interface import ProdutoRepositoryInterface
from app.application.interfaces.geral.produto_adapter_interface import ProdutoAdapterInterface
from app.domain.entities.produto_entity import ProdutoEntity
from app.infra.models.sqlalchemy.produto_model import ProdutoModel


@dataclass(slots=True, kw_only=True)
class PgProdutoRepository(ProdutoRepositoryInterface):
    session: Optional[Session] = None
    produto_adapter: ProdutoAdapterInterface

    def inserir_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        produto_model: ProdutoModel = self.produto_adapter.produto_entity_to_produto_model(data=produto_entity)
        self.session.add(produto_model)
        self.session.flush()

        return self.produto_adapter.produto_model_to_produto_entity(data=produto_model)
    
    def selecionar_produtos(self) -> List[ProdutoEntity]:
        produto_models: List[ProdutoModel] = self.session.query(ProdutoModel).filter(ProdutoModel.ativo == True).all()
        produto_entities: List[ProdutoEntity] = [
            self.produto_adapter.produto_model_to_produto_entity(data=produto_model)
            for produto_model in produto_models
        ]

        return produto_entities
    
    def selecionar_produto_por_id(self, produto_id: str) -> ProdutoEntity:
        produto_model: ProdutoModel = self.session.query(ProdutoModel).filter(
            ProdutoModel.id == produto_id,
            ProdutoModel.ativo == True
        ).first()
        if produto_model:
            return produto_model
        
        return False
    
    def atualizar_produto(self, produto_entity: ProdutoEntity) -> ProdutoEntity:
        produto_model: ProdutoModel = self.selecionar_produto_por_id(produto_id=produto_entity.id)

        if produto_model:
            produto_model.nome = produto_entity.nome
            produto_model.marca = produto_entity.marca
            produto_model.valor = produto_entity.valor
            produto_model.atualizado_em = produto_entity.atualizado_em

            self.session.add(produto_model)
            self.session.flush()

            return self.produto_adapter.produto_model_to_produto_entity(data=produto_model)
        
        return False
    
    def deletar_produto(self, produto_id: str) -> None:
        produto_model: ProdutoModel = self.selecionar_produto_por_id(produto_id=produto_id)

        if produto_model:
            produto_model.ativo = False
            self.session.add(produto_model)
            self.session.flush()

            return True

        return False
    