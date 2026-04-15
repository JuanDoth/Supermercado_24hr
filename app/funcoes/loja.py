from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_required, current_user
from bson import ObjectId
from app import produtos_col, pedidos_col

loja_bp = Blueprint('loja', __name__)

@loja_bp.route('/loja')
@login_required
def loja():
    produtos = list(produtos_col.find())
    return render_template('loja.html', produtos=produtos)

@loja_bp.route('/carrinho')
@login_required
def carrinho():
    itens = session.get('carrinho', [])
    total = sum(i['preco'] * i['qtd'] for i in itens)
    return render_template('carrinho.html', itens=itens, total=total)

@loja_bp.route('/adicionar_carrinho/<id>')
@login_required
def adicionar_carrinho(id):
    produto = produtos_col.find_one({'_id': ObjectId(id)})
    if produto:
        carrinho = session.get('carrinho', [])
        for item in carrinho:
            if item['id'] == str(id):
                item['qtd'] += 1
                session['carrinho'] = carrinho
                return redirect(url_for('loja.loja'))
        carrinho.append({
            'id': str(id),
            'nome': produto['nome'],
            'preco': produto['preco'],
            'qtd': 1
        })
        session['carrinho'] = carrinho
    return redirect(url_for('loja.loja'))

@loja_bp.route('/remover_carrinho/<id>')
@login_required
def remover_carrinho(id):
    carrinho = session.get('carrinho', [])
    session['carrinho'] = [i for i in carrinho if i['id'] != id]
    return redirect(url_for('loja.carrinho'))

@loja_bp.route('/finalizar_pedido', methods=['POST'])
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
    return redirect(url_for('loja.loja'))