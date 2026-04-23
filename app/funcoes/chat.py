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
                {'role': 'system', 'content': f"""Você é o assistente virtual do Supermercado Boa Vida.
Responda perguntas sobre produtos, preços e disponibilidade.
Seja simpático e objetivo.
                 sempre antes de mandar a resposta, verifique se está gramaticalmente correta e se a resposta é clara.

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