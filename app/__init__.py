from flask import Flask
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager
from app.auth.routes import auth_bp  # Importa o blueprint de autenticação
from app.db import get_db_connection  # Importa a função para conectar ao banco de dados

# Carrega variáveis de ambiente do .env
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configurações do Flask
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    # Inicializa o JWTManager com a aplicação Flask
    jwt = JWTManager(app)

    # Conecta ao banco de dados e garante que a conexão seja feita ao iniciar o app
    client = get_db_connection()  # Estabelece a conexão com o banco de dados
    if client:
        print("Conexão com o banco de dados estabelecida com sucesso!")

    # Registro do Blueprint de autenticação
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
