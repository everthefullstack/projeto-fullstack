from werkzeug.security import generate_password_hash, check_password_hash
from app.application.interfaces.geral.password_manager_interface import PasswordManagerInterface


class PasswordManager(PasswordManagerInterface):
    def hash(self, password: str) -> str:
        return generate_password_hash(password)

    def verify(self, password_hash: str, password: str) -> bool:
        return check_password_hash(password_hash, password)
