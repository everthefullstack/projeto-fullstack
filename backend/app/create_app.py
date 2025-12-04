from flask import Flask
from flask_cors import CORS
from app.presentation.routes import create_routes
from app.presentation.composers.database.table_create_composer import TableCreateComposer
from app.infra.settings import settings

def create_app():

    app: Flask = Flask(__name__)
    create_routes(app)

    CORS(app, 
         origins=settings.get_settings().ALLOWED_ORIGINS,
         methods=settings.get_settings().ALLOWED_METHODS,
         allow_headers=settings.get_settings().ALLOWED_HEADERS,
         supports_credentials=settings.get_settings().ALLOWED_CREDENTIALS)
    

    table = TableCreateComposer.compose()
    table.create_table()
    
    return app

def create_minimal_app():

    app: Flask = Flask(__name__)
    
    create_routes(app)
    CORS(app)

    table = TableCreateComposer.compose()
    table.create_table()

    return app
