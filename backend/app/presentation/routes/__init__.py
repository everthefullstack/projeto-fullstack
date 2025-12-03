from flask import Flask
from app.presentation.routes.index_routes import index_routes
from app.presentation.routes.auth_routes import auth_routes
from app.presentation.routes.usuario_routes import usuario_routes
from app.presentation.routes.produto_routes import produto_routes


def create_routes(app: Flask):
    app.register_blueprint(index_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(usuario_routes)
    app.register_blueprint(produto_routes)