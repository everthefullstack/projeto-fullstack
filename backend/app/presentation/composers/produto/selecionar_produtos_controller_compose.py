from app.presentation.adapters.produto_adapter import ProdutoAdapter
from app.infra.settings import settings
from app.infra.database.sqlalchemy import engine
from app.infra.database.sqlalchemy.session_manager import SessionManager
from app.infra.repositories.pg_produto_repository import PgProdutoRepository
from app.infra.unit_of_work.produto_unit_of_work import ProdutoUnitOfWork
from app.application.use_cases.produto.selecionar_produtos_use_case import SelecionarProdutosUseCase
from app.presentation.controllers.produto.selecionar_produtos_controller import SelecionarProdutosController


class SelecionarProdutosControllerComposer:

    @staticmethod
    def compose():
        
        produto_adapter = ProdutoAdapter()
        session = SessionManager(engine=engine).get_session()
        repository = PgProdutoRepository(produto_adapter=produto_adapter)
        unit_of_work = ProdutoUnitOfWork(session=session, produto_repository=repository)
        use_case = SelecionarProdutosUseCase(unit_of_work=unit_of_work)
        controller = SelecionarProdutosController(selecionar_produtos_use_case=use_case)

        return controller
