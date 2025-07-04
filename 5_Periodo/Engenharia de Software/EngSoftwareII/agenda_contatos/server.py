from flask import Flask, send_from_directory
from agenda_contatos.Controller.contato_controller import contato_bp
from agenda_contatos.Controller.categoria_controller import categoria_bp
from agenda_contatos.logger_singleton import Logger
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

app.register_blueprint(contato_bp)
app.register_blueprint(categoria_bp)
logger = Logger.get_instance()

@app.route("/")
def home():
    logger.info("Página inicial acessada")
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
