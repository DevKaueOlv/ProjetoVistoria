from app.db import get_db_connection

def add_record(data, user_id):
    """
    Adiciona um novo registro de vistoria ao banco de dados e cria uma relação entre o registro e o usuário.
    """
    client = get_db_connection()
    try:
        # Cria o registro de vistoria com as novas propriedades
        record = client.command(
            "INSERT INTO Registro SET vistoriador = '{}', data_vistoria = '{}', tipo_vistoria = '{}', tipo_imovel = '{}', endereco_imovel = '{}', locador = '{}', locatario = '{}', ambientes_caracteristicas = '{}', data = sysdate()".format(
                data['vistoriador'],
                data['data_vistoria'],
                data['tipo_vistoria'],
                data['tipo_imovel'],
                data['endereco_imovel'],
                data['locador'],
                data['locatario'],
                data['ambientes_caracteristicas']
            )
        )
        
        # Vincula o registro ao usuário usando a aresta CriadoPor
        client.command(
            "CREATE EDGE CriadoPor FROM (SELECT FROM Usuario WHERE @rid = {}) TO (SELECT FROM Registro WHERE @rid = '{}')".format(user_id, record[0]._rid)
        )
    finally:
        client.db_close()

def get_records():
    """
    Recupera todos os registros de vistoria do banco de dados.
    """
    client = get_db_connection()
    try:
        records = client.command("SELECT FROM Registro")
    finally:
        client.db_close()
    return records

def add_user(username, password_hash):
    """
    Adiciona um novo usuário ao banco de dados.
    """
    client = get_db_connection()
    try:
        client.command(
            "INSERT INTO Usuario SET username = '{}', password = '{}'".format(username, password_hash)
        )
    finally:
        client.db_close()

def get_user_by_username(username):
    """
    Recupera um usuário com base no nome de usuário fornecido.
    """
    client = get_db_connection()
    try:
        result = client.command("SELECT FROM Usuario WHERE username = '{}'".format(username))
    finally:
        client.db_close()
    return result[0] if result else None
