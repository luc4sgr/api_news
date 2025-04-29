from flask import Flask

def create_app():
    app = Flask(__name__)

    # Aqui já poderíamos registrar rotas, config, extensões
    return app
