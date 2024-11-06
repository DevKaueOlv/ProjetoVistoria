from app import create_app
import logging
from logging import StreamHandler

app = create_app()

# Ativando logs detalhados
app.config['DEBUG'] = True
app.logger.addHandler(StreamHandler())
app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.run(debug=True)
