from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from app.models import add_record, get_records, get_user_by_username

auth_bp = Blueprint('auth', __name__)

# Rota de Teste
@auth_bp.route('/test', methods=['GET'])
def test():
    return jsonify({"msg": "Rota de teste está funcionando!"}), 200

# Rota de Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Busca o usuário no banco de dados
    user = get_user_by_username(username)
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user._rid)  # Salva o RID do usuário como identidade
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Credenciais inválidas"}), 401

# Rota Protegida
@auth_bp.route('/protected', methods=['GET'])
@jwt_required()  # Protege a rota
def protected():
    return jsonify({"msg": "Esta é uma rota protegida!"}), 200

# Rota de Criação de Registros
@auth_bp.route('/records', methods=['POST'])
@jwt_required()
def create_record():
    data = request.get_json()
    
    # Verifica se todos os campos obrigatórios estão presentes na requisição
    required_fields = [
        "vistoriador", "data_vistoria", "tipo_vistoria", "tipo_imovel", 
        "endereco_imovel", "locador", "locatario", "ambientes_caracteristicas"
    ]
    
    for field in required_fields:
        if field not in data:
            return jsonify({"msg": f"Campo {field} é obrigatório"}), 400

    user_id = get_jwt_identity()  # Obtém o ID do usuário autenticado
    add_record(data, user_id)
    return jsonify({"msg": "Registro criado com sucesso!"}), 201

