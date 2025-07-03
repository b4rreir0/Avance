# Factory de la aplicación
from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configuración inicial
    return app