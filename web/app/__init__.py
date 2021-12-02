from flask import Flask
from config import Config

app = Flask(__name__, template_folder = './templates')
app.config.from_object(Config)

from app.routes import main_bp
from app.api import api
app.register_blueprint(main_bp)
app.register_blueprint(api)