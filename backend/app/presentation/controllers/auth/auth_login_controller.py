from dataclasses import dataclass
from app.application.interfaces.auth.auth_use_case_interface import AuthLoginUseCaseInterface
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.domain.value_objects.auth_value_object import AuthValueObject
from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.domain.erros.erros import ErroDeValueObject


@dataclass(slots=True, kw_only=True)
class AuthLoginController:

    auth_login_use_case: AuthLoginUseCaseInterface

    def login(self, http_request_value_object: HttpRequestValueObject) -> HttpResponseValueObject:
        try:
            auth_value_object: AuthValueObject = AuthValueObject(
                login=http_request_value_object.body.get("login"),
                senha=http_request_value_object.body.get("senha"),
            )
            
            auth_login_response = self.auth_login_use_case.login(auth_value_object=auth_value_object)
            
            return HttpResponseValueObject(status_code=200, body={"data": DataclassAdapter().dataclass_to_dict(data=auth_login_response)})

        except ErroDeValueObject as e:
            return HttpResponseValueObject(status_code=422, message=f"{e.args[0]}")
        
        except Exception as e:
            return HttpResponseValueObject(status_code=500, message=f"Erro interno do servidor. {e}") 