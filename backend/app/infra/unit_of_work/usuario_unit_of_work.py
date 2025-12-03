from dataclasses import dataclass
from app.application.interfaces.geral.database_manager_interface import SessionManagerInterface
from app.application.interfaces.geral.unit_of_work_interface import UnitOfWorkInterface
from app.domain.interfaces.usuario_repository_interface import UsuarioRepositoryInterface


@dataclass(slots=True, kw_only=True)
class UsuarioUnitOfWork(UnitOfWorkInterface):

    session: SessionManagerInterface
    usuario_repository: UsuarioRepositoryInterface

    def __enter__(self) -> "UnitOfWorkInterface":

        self.usuario_repository.session = self.session
       
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is None:
            self.session.commit()

        else:
            self.session.rollback()

        self.session.close()
