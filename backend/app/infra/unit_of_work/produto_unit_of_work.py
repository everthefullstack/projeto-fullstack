from dataclasses import dataclass
from app.application.interfaces.geral.database_manager_interface import SessionManagerInterface
from app.application.interfaces.geral.unit_of_work_interface import UnitOfWorkInterface
from app.domain.interfaces.produto_repository_interface import ProdutoRepositoryInterface


@dataclass(slots=True, kw_only=True)
class ProdutoUnitOfWork(UnitOfWorkInterface):

    session: SessionManagerInterface
    produto_repository: ProdutoRepositoryInterface

    def __enter__(self) -> "UnitOfWorkInterface":

        self.produto_repository.session = self.session
       
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.session.commit()

        else:
            self.session.rollback()

        self.session.close()
