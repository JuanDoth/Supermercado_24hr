from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'supermercado_boa_vida_2024'

client = MongoClient('mongodb://localhost:27017/')
db = client['supermercado']
produtos_col = db['produtos']
usuarios_col = db['usuarios']
pedidos_col = db['pedidos']

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import routes