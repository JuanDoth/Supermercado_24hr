import os
from dotenv import load_dotenv

load_dotenv()

GROQ_KEY = os.getenv('GROQ_KEY')
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_TOKEN = os.getenv('TWILIO_TOKEN')
TWILIO_NUMERO = os.getenv('TWILIO_NUMERO')
LOJA_NUMERO = os.getenv('LOJA_NUMERO')