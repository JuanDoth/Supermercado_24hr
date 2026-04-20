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
login_manager.login_view = 'contas.login'


from app.funcoes import contas_bp, loja_bp, admin_bp, chat_bp
from app.funcoes.modelos import Usuario
from bson import ObjectId

app.register_blueprint(contas_bp)
app.register_blueprint(loja_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(chat_bp)

@login_manager.user_loader
def load_user(user_id):
    u = usuarios_col.find_one({'_id': ObjectId(user_id)})
    if u:
        return Usuario(str(u['_id']), u['nome'], u['email'], u.get('is_admin', False))
    return None