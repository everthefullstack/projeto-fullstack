from app.application.interfaces.geral.produto_adapter_interface import ProdutoAdapterInterface
from app.domain.entities.produto_entity import ProdutoEntity
from app.infra.models.sqlalchemy.produto_model import ProdutoModel


class ProdutoAdapter(ProdutoAdapterInterface):
    @staticmethod
    def produto_entity_to_produto_model(data: ProdutoEntity) -> ProdutoModel:
        return ProdutoModel(nome=data.nome, 
                            marca=data.marca, 
                            valor=data.valor,
                            criado_em=data.criado_em if hasattr(data, 'criado_em') else None,
                            atualizado_em=data.atualizado_em if hasattr(data, 'atualizado_em') else None)
    
    @staticmethod
    def produto_model_to_produto_entity(data: ProdutoModel) -> ProdutoEntity:
        return ProdutoEntity(id=data.id,
                             nome=data.nome, 
                             marca=data.marca, 
                             valor=data.valor,
                             criado_em=data.criado_em,
                             atualizado_em=data.atualizado_em)
