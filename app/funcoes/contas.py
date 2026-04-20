from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import usuarios_col
from app.funcoes.modelos import Usuario, ADMIN_EMAIL, ADMIN_SENHA

contas_bp = Blueprint('contas', __name__)

@contas_bp.route('/')
@ contas_bp.route('/index')
def index():
    return render_template('index.html')

@contas_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
            login_user(Usuario('admin', 'Administrador', ADMIN_EMAIL, is_admin=True))
            return redirect(url_for('admin.catalogo'))
        u = usuarios_col.find_one({'email': email})
        if u and check_password_hash(u['senha'], senha):
            login_user(Usuario(str(u['_id']), u['nome'], u['email']))
            return redirect(url_for('loja.loja'))
        flash('Email ou senha incorretos.')
    return render_template('login.html')

@contas_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        if usuarios_col.find_one({'email': email}):
            flash('Este email já está cadastrado.')
            return render_template('cadastro.html')
        usuarios_col.insert_one({
            'nome': nome,
            'email': email,
            'senha': generate_password_hash(senha)
        })
        flash('Cadastro realizado! Faça login.')
        return redirect(url_for('auth.login'))
    return render_template('cadastro.html')

@contas_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('contas.index'))