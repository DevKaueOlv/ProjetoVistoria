import os

# Gerar uma chave secreta para Flask
flask_secret_key = os.urandom(24).hex()
print("FLASK_SECRET_KEY:", flask_secret_key)

# Gerar uma chave secreta para JWT
jwt_secret_key = os.urandom(24).hex()
print("JWT_SECRET_KEY:", jwt_secret_key)
