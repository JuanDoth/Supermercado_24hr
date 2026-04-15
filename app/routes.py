from groq import Groq
from twilio.rest import Client as TwilioClient
from app import app, produtos_col, usuarios_col, pedidos_col
from flask import render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager




@app.route('/chat', methods=['POST'])
def chat():
    mensagem = request.json.get('mensagem', '')

    produtos = list(produtos_col.find())
    lista_produtos = '\n'.join([
        f"- {p['nome']}: R$ {p['preco']:.2f}"
        for p in produtos
    ])

    cliente_groq = Groq(api_key=GROQ_KEY)

    resposta = cliente_groq.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role': 'system', 'content': f"""Você é o assistente virtual do Supermercado Boa Vida.
Responda perguntas sobre produtos, preços e disponibilidade.
Se o cliente quiser fazer um pedido, confirme os itens e diga que vai enviar para a loja.
Seja simpático e objetivo.

Produtos disponíveis:
{lista_produtos}"""},
            {'role': 'user', 'content': mensagem}
        ]
    )

    texto_resposta = resposta.choices[0].message.content

    if any(palavra in mensagem.lower() for palavra in ['pedido', 'quero', 'comprar', 'pedir']):
        twilio = TwilioClient(TWILIO_SID, TWILIO_TOKEN)
        twilio.messages.create(
            from_=TWILIO_NUMERO,
            to=LOJA_NUMERO,
            body=f"Novo pedido pelo site!\nCliente: {current_user.nome}\nMensagem: {mensagem}"
        )

    return {'resposta': texto_resposta}

# Admin fixo
ADMIN_EMAIL = 'admin@boavida.com'
ADMIN_SENHA = 'admin123'

class Usuario(UserMixin):
    def __init__(self, id, nome, email, is_admin=False):
        self.id = str(id)
        self.nome = nome
        self.email = email
        self.is_admin = is_admin

@login_manager.user_loader
def load_user(user_id):
    if user_id == 'admin':
        return Usuario('admin', 'Administrador', ADMIN_EMAIL, is_admin=True)
    u = usuarios_col.find_one({'_id': ObjectId(user_id)})
    if u:
        return Usuario(str(u['_id']), u['nome'], u['email'])
    return None

# ── PÁGINAS PÚBLICAS ──

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
            admin = Usuario('admin', 'Administrador', ADMIN_EMAIL, is_admin=True)
            login_user(admin)
            return redirect(url_for('catalogo'))

        u = usuarios_col.find_one({'email': email})
        if u and check_password_hash(u['senha'], senha):
            login_user(Usuario(str(u['_id']), u['nome'], u['email']))
            return redirect(url_for('loja'))

        flash('Email ou senha incorretos.')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
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
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# ── LOJA (CLIENTES) ──

@app.route('/loja')
@login_required
def loja():
    produtos = list(produtos_col.find())
    return render_template('loja.html', produtos=produtos)

@app.route('/carrinho')
@login_required
def carrinho():
    itens = session.get('carrinho', [])
    total = sum(i['preco'] * i['qtd'] for i in itens)
    return render_template('carrinho.html', itens=itens, total=total)

@app.route('/adicionar_carrinho/<id>')
@login_required
def adicionar_carrinho(id):
    produto = produtos_col.find_one({'_id': ObjectId(id)})
    if produto:
        carrinho = session.get('carrinho', [])
        for item in carrinho:
            if item['id'] == str(id):
                item['qtd'] += 1
                session['carrinho'] = carrinho
                return redirect(url_for('loja'))
        carrinho.append({
            'id': str(id),
            'nome': produto['nome'],
            'preco': produto['preco'],
            'qtd': 1
        })
        session['carrinho'] = carrinho
    return redirect(url_for('loja'))

@app.route('/remover_carrinho/<id>')
@login_required
def remover_carrinho(id):
    carrinho = session.get('carrinho', [])
    session['carrinho'] = [i for i in carrinho if i['id'] != id]
    return redirect(url_for('carrinho'))

@app.route('/finalizar_pedido', methods=['POST'])
@login_required
def finalizar_pedido():
    itens = session.get('carrinho', [])
    if itens:
        pedidos_col.insert_one({
            'usuario_id': current_user.id,
            'usuario_nome': current_user.nome,
            'itens': itens,
            'total': sum(i['preco'] * i['qtd'] for i in itens)
        })
        session['carrinho'] = []
        flash('Pedido realizado com sucesso!')
    return redirect(url_for('loja'))

# ── ADMIN ──

@app.route('/catalogo')
@login_required
def catalogo():
    if not current_user.is_admin:
        return redirect(url_for('loja'))
    produtos = list(produtos_col.find())
    return render_template('catalogo.html', produtos=produtos)

@app.route('/adicionar', methods=['POST'])
@login_required
def adicionar():
    if not current_user.is_admin:
        return redirect(url_for('loja'))
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    if nome and preco:
        produtos_col.insert_one({
            'nome': nome,
            'preco': float(preco),
        })
    return redirect(url_for('catalogo'))

@app.route('/editar/<id>')
@login_required
def editar(id):
    if not current_user.is_admin:
        return redirect(url_for('loja'))
    produto = produtos_col.find_one({'_id': ObjectId(id)})
    return render_template('editar.html', produto=produto)

@app.route('/atualizar/<id>', methods=['POST'])
@login_required
def atualizar(id):
    if not current_user.is_admin:
        return redirect(url_for('loja'))
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    if nome and preco:
        produtos_col.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'nome': nome, 'preco': float(preco),}}
        )
    return redirect(url_for('catalogo'))

@app.route('/deletar/<id>', methods=['POST'])
@login_required
def deletar(id):
    if not current_user.is_admin:
        return redirect(url_for('loja'))
    produtos_col.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('catalogo'))

@app.route('/pedidos')
@login_required
def pedidos():
    if not current_user.is_admin:
        return redirect(url_for('loja'))
    todos = list(pedidos_col.find())
    return render_template('pedidos.html', pedidos=todos)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html',
        email='blablabla@gmail.com',
        celular=859432478,
        instagram='Showdebola_arretado')