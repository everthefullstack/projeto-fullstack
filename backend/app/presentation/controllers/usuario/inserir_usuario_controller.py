from dataclasses import dataclass
from app.application.interfaces.usuario.usuario_use_case_interface import InserirUsuarioUseCaseInterface
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.domain.entities.usuario_entity import UsuarioEntity
from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.domain.erros.erros import ErroDeDominio


@dataclass(slots=True, kw_only=True)
class InserirUsuarioController:

    inserir_usuario_use_case: InserirUsuarioUseCaseInterface

    def inserir_usuario(self, http_request_value_object: HttpRequestValueObject) -> HttpResponseValueObject:
        try:
            usuario_entity: UsuarioEntity = UsuarioEntity(
                usuario=http_request_value_object.body.get("usuario"),
                email=http_request_value_object.body.get("email"),
                senha=http_request_value_object.body.get("senha"),
            )
            
            usuario_response = self.inserir_usuario_use_case.inserir_usuario(usuario_entity=usuario_entity)

            return HttpResponseValueObject(status_code=202, body=DataclassAdapter().dataclass_to_dict(data=usuario_response))

        except ErroDeDominio as e:
            return HttpResponseValueObject(status_code=422, message=f"{e.args[0]}")
        
        except Exception as e:
            return HttpResponseValueObject(status_code=500, message=f"Erro interno do servidor. {e}")