from flask_login import UserMixin

ADMIN_EMAIL = 'admin@boavida.com'
ADMIN_SENHA = 'admin123'

class Usuario(UserMixin):
    def __init__(self, id, nome, email, is_admin=False):
        self.id = str(id)
        self.nome = nome
        self.email = email
        self.is_admin = is_admin