from flask import Blueprint, request
from flask_login import current_user
from groq import Groq
from twilio.rest import Client as TwilioClient
from app import produtos_col
from app.funcoes.config import GROQ_KEY, TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMERO, LOJA_NUMERO

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    mensagem = request.json.get('mensagem', '')
    produtos = list(produtos_col.find())
    lista_produtos = '\n'.join([
        f"- {p['nome']}: R$ {p['preco']:.2f}" for p in produtos
    ])

    cliente_groq = Groq(api_key=GROQ_KEY)
    resposta = cliente_groq.chat.completions.create(
        model='llama-3.3-70b-versatile',
        messages=[
            {'role': 'system', 'content': f"""Você é o assistente virtual do Supermercado Boa Vida.
Responda perguntas sobre produtos, preços e disponibilidade.
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
            body=f"Novo pedido!\nCliente: {current_user.nome}\nMensagem: {mensagem}"
        )

    return {'resposta': texto_resposta}