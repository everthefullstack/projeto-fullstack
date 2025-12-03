from flask import Flask
from app.presentation.routes import create_routes
from app.presentation.composers.database.table_create_composer import TableCreateComposer


def create_app():

    app: Flask = Flask(__name__)

    create_routes(app)

    table = TableCreateComposer.compose()
    table.create_table()
    
    return app

def create_minimal_app():

    app: Flask = Flask(__name__)

    create_routes(app)

    table = TableCreateComposer.compose()
    table.create_table()

    return app
