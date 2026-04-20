from flask_login import current_user
from flask import Blueprint, request
from groq import Groq
from app import produtos_col
from app.funcoes.config import GROQ_KEY

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    if not current_user.is_authenticated:
        return {'resposta': 'Você precisa fazer login para conversar comigo! 😊'}, 401

    mensagem = request.json.get('mensagem', '')
    produtos = list(produtos_col.find())
    lista_produtos = '\n'.join([
        f"- {p['nome']}: R$ {p['preco']:.2f}" for p in produtos
    ])

    try:
        cliente_groq = Groq(api_key=GROQ_KEY)
        resposta = cliente_groq.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[
                {'role': 'system', 'content': f"""Você é um assistente de vendas para uma loja de produtos eletrônicos. Ajude os clientes a encontrar o produto certo com base em suas necessidades e preferências. Seja amigável, prestativo e forneça informações claras sobre os produtos disponíveis.

Produtos disponíveis:
{lista_produtos}"""},
                {'role': 'user', 'content': mensagem}
            ]
        )
        texto_resposta = resposta.choices[0].message.content
    except Exception as e:
        print(f"Erro na IA: {e}")
        return {'resposta': f'Erro: {str(e)}'}

    return {'resposta': texto_resposta}