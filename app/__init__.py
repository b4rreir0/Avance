# Factory de la aplicaci�n
from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configuraci�n inicial
    return app