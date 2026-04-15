# 🛒 Supermercado Boa Vida - Plataforma Web

Plataforma de e-commerce para o Supermercado Boa Vida, desenvolvida em Flask com integração de IA, sistema de autenticação e gerenciamento de pedidos.

## 📋 Descrição do Projeto

Um sistema web completo de vendas online que permite clientes fazer compras e administradores gerenciar o catálogo de produtos. A plataforma conta com um assistente virtual baseado em IA (Groq) e integração com WhatsApp (Twilio) para notificações de pedidos.

## ✨ Funcionalidades Implementadas

### 🔐 Autenticação e Usuários
- [x] Sistema de cadastro de usuários
- [x] Login seguro com hash de senha (Werkzeug)
- [x] Autenticação com Flask-Login
- [x] Admin fixo para gerenciamento
- [x] Logout seguro

### 🛍️ Loja para Clientes
- [x] Visualização de produtos com preços
- [x] Carrinho de compras com sessão
- [x] Adicionar produtos ao carrinho
- [x] Remover produtos do carrinho
- [x] Finalizar pedidos
- [x] Histórico de compras

### 🤖 Assistente Virtual (IA)
- [x] Chat inteligente com IA Groq (Llama 3.3 70B)
- [x] Responde sobre produtos e preços
- [x] Integração com Twilio para envio de pedidos via SMS
- [x] Notificações automáticas à loja

### 👨‍💼 Painel Administrativo
- [x] Visualizar catálogo de produtos
- [x] Adicionar novos produtos
- [x] Editar produtos existentes
- [x] Deletar produtos
- [x] Visualizar todos os pedidos
- [x] Ver página de contatos

## 🛠️ Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Banco de Dados:** MongoDB
- **Autenticação:** Flask-Login, Werkzeug
- **IA:** Groq API (Llama 3.3 70B)
- **SMS:** Twilio
- **ORM:** PyMongo (BSON)
- **Frontend:** HTML/CSS/JavaScript

## 📁 Estrutura do Projeto

```
Projetos_python/
├── README.md
├── app/
│   ├── __init__.py           # Inicialização da app Flask e conexão MongoDB
│   ├── routes.py             # Todas as rotas e endpoints
│   └── templates/            # Arquivos HTML
│       ├── index.html
│       ├── login.html
│       ├── cadastro.html
│       ├── loja.html
│       ├── carrinho.html
│       ├── catalogo.html
│       ├── editar.html
│       ├── pedidos.html
│       ├── contatos.html
│       └── ...
└── requirements.txt          # Dependências do projeto
```

## 🚀 Como Usar

### 1. Configuração Inicial

Clone ou baixe o projeto:
```bash
cd c:\Users\juand\OneDrive\Desktop\Cursos\Projetos_python
```

### 2. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:
```
GROQ_KEY=sua_chave_api_groq
TWILIO_SID=seu_twilio_sid
TWILIO_TOKEN=seu_twilio_token
TWILIO_NUMERO=seu_numero_twilio
LOJA_NUMERO=numero_da_loja
```

### 4. Executar a Aplicação

```bash
python app.py
```

Acesse em: `http://localhost:5000`

## 👤 Credenciais de Teste

### Admin
- **Email:** admin@boavida.com
- **Senha:** admin123

## 📋 Rotas da API

### Públicas
| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/login` | GET, POST | Login de usuários |
| `/cadastro` | GET, POST | Registro de novos usuários |
| `/contatos` | GET | Página de contatos |

### Autenticadas (Clientes)
| Rota | Método | Descrição |
|------|--------|-----------|
| `/loja` | GET | Exibir produtos |
| `/carrinho` | GET | Ver carrinho |
| `/adicionar_carrinho/<id>` | GET | Adicionar produto |
| `/remover_carrinho/<id>` | GET | Remover produto |
| `/finalizar_pedido` | POST | Confirmar compra |
| `/logout` | GET | Sair da conta |

### Admin
| Rota | Método | Descrição |
|------|--------|-----------|
| `/catalogo` | GET | Gerenciar produtos |
| `/adicionar` | POST | Adicionar produto |
| `/editar/<id>` | GET | Formulário de edição |
| `/atualizar/<id>` | POST | Salvar alterações |
| `/deletar/<id>` | POST | Remover produto |
| `/pedidos` | GET | Ver todos os pedidos |

### IA
| Rota | Método | Descrição |
|------|--------|-----------|
| `/chat` | POST | Chat com assistente IA |

## 💾 Banco de Dados

Coleções MongoDB:
- **produtos_col:** Nome, preço
- **usuarios_col:** Nome, email, senha (hash)
- **pedidos_col:** Usuario ID, nome, itens, total

## 🔄 Fluxo de Pedidos

1. Cliente faz login
2. Navega pela loja e adiciona produtos ao carrinho
3. Pode usar o chat de IA para tirar dúvidas
4. Finaliza o pedido
5. Loja recebe notificação via SMS/WhatsApp (Twilio)
6. Admin visualiza o pedido no painel

## ⚙️ Integração IA

O assistente virtual:
- Usa Groq API com modelo Llama 3.3 70B
- Acessa lista atualizada de produtos
- Detecta palavras-chave (pedido, comprar, pedir)
- Envia notificações automáticas à loja via Twilio

## 📱 Informações de Contato

- **Email:** blablabla@gmail.com
- **Celular:** 85 9432-478
- **Instagram:** @Showdebola_arretado

## 🐛 Próximas Melhorias

- [ ] Validação mais robusta de entrada
- [ ] Sistema de pagamento
- [ ] Rastreamento de pedidos
- [ ] Avaliações de produtos
- [ ] Email de confirmação
- [ ] Relatórios administrativos
- [ ] API RESTful completa

## 📝 Notas de Desenvolvimento

- Admin é fixo (não pode ser alterado)
- Senhas são criptografadas com bcrypt
- Carrinho armazenado em sessão (cliente)
- MongoDB armazena dados persistentes

---

**Desenvolvido por:** Juand  
**Última atualização:** 15 de abril de 2026  
**Status:** 🚧 Em desenvolvimento