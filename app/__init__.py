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
login_manager.login_view = 'auth.login'


from app.funcoes import auth_bp, loja_bp, admin_bp, chat_bp
from app.funcoes.modelos import Usuario
from bson import ObjectId

app.register_blueprint(auth_bp)
app.register_blueprint(loja_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(chat_bp)

@login_manager.user_loader
def load_user(user_id):
    from app.funcoes.modelos import ADMIN_EMAIL
    if user_id == 'admin':
        return Usuario('admin', 'Administrador', ADMIN_EMAIL, is_admin=True)
    u = usuarios_col.find_one({'_id': ObjectId(user_id)})
    if u:
        return Usuario(str(u['_id']), u['nome'], u['email'])
    return None