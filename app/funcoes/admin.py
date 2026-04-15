from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from bson import ObjectId
from app import produtos_col, pedidos_col

admin_bp = Blueprint('admin', __name__)

def apenas_admin():
    return not current_user.is_admin

@admin_bp.route('/catalogo')
@login_required
def catalogo():
    if apenas_admin():
        return redirect(url_for('loja.loja'))
    produtos = list(produtos_col.find())
    return render_template('catalogo.html', produtos=produtos)

@admin_bp.route('/adicionar', methods=['POST'])
@login_required
def adicionar():
    if apenas_admin():
        return redirect(url_for('loja.loja'))
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    if nome and preco:
        produtos_col.insert_one({'nome': nome, 'preco': float(preco)})
    return redirect(url_for('admin.catalogo'))

@admin_bp.route('/editar/<id>')
@login_required
def editar(id):
    if apenas_admin():
        return redirect(url_for('loja.loja'))
    produto = produtos_col.find_one({'_id': ObjectId(id)})
    return render_template('editar.html', produto=produto)

@admin_bp.route('/atualizar/<id>', methods=['POST'])
@login_required
def atualizar(id):
    if apenas_admin():
        return redirect(url_for('loja.loja'))
    nome = request.form.get('nome')
    preco = request.form.get('preco')
    if nome and preco:
        produtos_col.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'nome': nome, 'preco': float(preco)}}
        )
    return redirect(url_for('admin.catalogo'))

@admin_bp.route('/deletar/<id>', methods=['POST'])
@login_required
def deletar(id):
    if apenas_admin():
        return redirect(url_for('loja.loja'))
    produtos_col.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('admin.catalogo'))

@admin_bp.route('/pedidos')
@login_required
def pedidos():
    if apenas_admin():
        return redirect(url_for('loja.loja'))
    todos = list(pedidos_col.find())
    return render_template('pedidos.html', pedidos=todos)