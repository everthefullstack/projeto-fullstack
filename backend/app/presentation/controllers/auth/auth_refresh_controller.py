from dataclasses import dataclass
from app.application.interfaces.auth.auth_use_case_interface import AuthRefreshUseCaseInterface
from app.domain.value_objects.http_request_value_object import HttpRequestValueObject
from app.domain.value_objects.http_response_value_object import HttpResponseValueObject
from app.presentation.adapters.dataclass_adapter import DataclassAdapter
from app.domain.erros.erros import ErroDeValueObject


@dataclass(slots=True, kw_only=True)
class AuthRefreshController:

    auth_refresh_use_case: AuthRefreshUseCaseInterface

    def login(self, http_request_value_object: HttpRequestValueObject) -> HttpResponseValueObject:
        try:
            
            refresh_token: str = http_request_value_object.headers.get("Authorization", "").replace("Bearer ", "")
            auth_refresh_response = self.auth_refresh_use_case.refresh(refresh_token=refresh_token)
            
            return HttpResponseValueObject(status_code=200, body=DataclassAdapter().dataclass_to_dict(data=auth_refresh_response))

        except ErroDeValueObject as e:
            return HttpResponseValueObject(status_code=422, message=f"{e.args[0]}")
        
        except Exception as e:
            return HttpResponseValueObject(status_code=500, message=f"Erro interno do servidor. {e}") 