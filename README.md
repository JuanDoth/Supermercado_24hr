# 🛒 Supermercado Boa Vida - Plataforma Web

Uma plataforma completa de e-commerce para o Supermercado Boa Vida, desenvolvida em Flask com integração de IA (Groq), autenticação segura e gerenciamento avançado de pedidos.

**Status:** 🚧 Em desenvolvimento  
**Versão:** 1.0.0  
**Última atualização:** Abril de 2026

## 📋 Descrição do Projeto

Um sistema web de vendas online completo que permite clientes fazer compras e administradores gerenciar eficientemente o catálogo de produtos. A plataforma se destaca pela integração de um assistente virtual inteligente baseado em IA (Groq Llama 3.3 70B).

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
- [x] Recomendações personalizadas de produtos

### 👨‍💼 Painel Administrativo
- [x] Visualizar catálogo de produtos
- [x] Adicionar novos produtos
- [x] Editar produtos existentes
- [x] Deletar produtos
- [x] Visualizar todos os pedidos
- [x] Ver página de contatos

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| **Python** | 3.8+ | Linguagem base |
| **Flask** | 2.x | Framework web |
| **MongoDB** | 4.4+ | Banco de dados NoSQL |
| **Flask-Login** | 0.6+ | Autenticação e sessões |
| **Werkzeug** | 2.x | Hash de senhas (PBKDF2) |
| **Groq API** | - | IA (Llama 3.3 70B) |
| **PyMongo** | 4.x | Driver MongoDB |
| **python-dotenv** | - | Variáveis de ambiente |

## 📋 Funcionalidades Implementadas

### 🔐 Autenticação e Usuários
- ✅ Sistema de cadastro com validação de email
- ✅ Login seguro com hash de senha (PBKDF2 via Werkzeug)
- ✅ Autenticação gerenciada com Flask-Login
- ✅ Admin fixo para acesso administrativo
- ✅ Logout com limpeza de sessão
- ✅ Recuperação segura de sessão

### 🛍️ Loja para Clientes
- ✅ Catálogo de produtos com filtros
- ✅ Visualização detalhada de produtos
- ✅ Carrinho de compras persistente em sessão
- ✅ Adicionar/remover produtos do carrinho
- ✅ Cálculo automático de totais
- ✅ Finalizar pedidos com confirmação
- ✅ Histórico completo de compras
- ✅ Acompanhamento de pedidos

### 🤖 Assistente Virtual (IA)
- ✅ Chat inteligente com Groq (Llama 3.3 70B)
- ✅ Respostas contextualizadas sobre produtos e preços
- ✅ Detecção automática de intenção de compra
- ✅ Histórico de conversa mantido

### 👨‍💼 Painel Administrativo
- ✅ Dashboard com estatísticas
- ✅ Gerenciamento completo de produtos (CRUD)
- ✅ Visualização em tempo real de pedidos
- ✅ Filtros e busca avançada
- ✅ Página de contatos e informações
- ✅ Relatório de vendas por período

## 📁 Estrutura do Projeto

```
Projetos_python/
├── projeto_loja.py              # Entry point da aplicação
├── README.md                    # Este arquivo
├── requirements.txt             # Dependências Python
├── .env                         # Variáveis de ambiente (não versionado)
├── .gitignore                   # Arquivos ignorados pelo Git
│
└── app/
    ├── __init__.py              # Inicialização Flask e conexão MongoDB
    ├── funcoes/
    │   ├── __init__.py
    │   ├── config.py            # Configurações e variáveis de ambiente
    │   ├── modelos.py           # Modelos de dados (User, Product, Order)
    │   ├── contas.py            # Rotas de autenticação (login, cadastro, logout)
    │   ├── loja.py              # Rotas da loja (catálogo, carrinho, pedidos)
    │   ├── admin.py             # Rotas administrativas (CRUD produtos, pedidos)
    │   └── chat.py              # Chat com IA (Groq)
    │
    ├── static/
    │   └── style.css            # Estilos CSS da aplicação
    │
    └── templates/
        ├── base.html            # Template base (herança)
        ├── index.html           # Página inicial/home
        ├── login.html           # Formulário de login
        ├── cadastro.html        # Formulário de cadastro
        ├── loja.html            # Catálogo de produtos
        ├── carrinho.html        # Carrinho de compras
        ├── catalogo.html        # Gerenciamento de produtos (admin)
        ├── editar.html          # Edição de produtos (admin)
        ├── pedidos.html         # Visualização de pedidos
        └── contatos.html        # Página de contatos
```

## 📋 Requisitos do Sistema

### Hardware Mínimo
- Processador: 1.5 GHz
- RAM: 2 GB
- Espaço em disco: 500 MB

### Software Necessário
- Python 3.8 ou superior
- MongoDB 4.4 ou superior (local ou cloud)
- Conexão de internet (APIs externas)

## 🚀 Como Usar

### 1. Pré-requisitos
Certifique-se de ter instalado:
- Python 3.8+
- pip (gerenciador de pacotes Python)
- MongoDB (local ou MongoDB Atlas)
- Git (opcional)

### 2. Clonar ou Baixar o Projeto

**Via Git:**
```bash
git clone https://github.com/seu_usuario/supermercado-boa-vida.git
cd Projetos_python
```

**Manual:**
Baixe o arquivo ZIP e extraia na pasta desejada.

### 3. Criar Ambiente Virtual

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Windows (CMD)
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Groq API
GROQ_KEY=sua_chave_api_groq_aqui

# MongoDB
MONGODB_URI=mongodb+srv://usuario:senha@cluster.mongodb.net/supermercado?retryWrites=true&w=majority
# OU para MongoDB local:
MONGODB_URI=mongodb://localhost:27017/supermercado

# Flask
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta_segura
```

**Como obter as chaves:**
- **Groq API Key:** https://console.groq.com/keys
- **MongoDB Atlas:** https://www.mongodb.com/cloud/atlas

### 6. Executar a Aplicação

```bash
python projeto_loja.py
```

A aplicação estará disponível em: **http://localhost:5000**

## 👤 Credenciais Padrão

### Usuário Administrador
- **Email:** testeadmin@gmail.com
- **Senha:** admin123

> ⚠️ **Importante:** Altere a senha do admin em produção!

### Usuário de Teste (Cliente)
- **Email:** cliente@example.com
- **Senha:** senha123

## 📚 Guia de Uso

### Para Clientes

1. **Criar Conta**
   - Clique em "Cadastro"
   - Preencha os dados (nome, email, senha)
   - Clique em "Cadastrar"

2. **Fazer Login**
   - Acesse http://localhost:5000/login
   - Digite suas credenciais
   - Clique em "Entrar"

3. **Navegar na Loja**
   - Visualize produtos em /loja
   - Clique em "Adicionar ao Carrinho"
   - Veja o carrinho em /carrinho

4. **Fazer um Pedido**
   - Adicione produtos ao carrinho
   - Clique em "Finalizar Pedido"
   - Confirme a compra

5. **Chat com IA**
   - Converse com o assistente
   - Faça perguntas sobre produtos
   - Peça sugestões

### Para Administradores

1. **Acessar Painel Admin**
   - Login com credenciais do admin
   - Você terá acesso às funções administrativas

2. **Gerenciar Produtos**
   - Acesse /catalogo
   - Clique em "Adicionar Novo Produto"
   - Preencha: nome, preço, descrição
   - Edite ou delete conforme necessário

3. **Visualizar Pedidos**
   - Acesse /pedidos
   - Veja todos os pedidos em tempo real
   - Filtre por data, cliente ou status

## 📡 Rotas e Endpoints

### Rotas Públicas
| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Página inicial |
| `/login` | GET, POST | Autenticação de usuários |
| `/cadastro` | GET, POST | Registro de novos usuários |
| `/contatos` | GET | Página de contatos |

### Rotas Autenticadas (Clientes)
| Rota | Método | Descrição |
|------|--------|-----------|
| `/loja` | GET | Exibir catálogo de produtos |
| `/carrinho` | GET | Visualizar carrinho de compras |
| `/adicionar_carrinho/<id>` | GET | Adicionar produto ao carrinho |
| `/remover_carrinho/<id>` | GET | Remover produto do carrinho |
| `/finalizar_pedido` | POST | Confirmar e processar compra |
| `/pedidos` | GET | Ver histórico de pedidos do cliente |
| `/logout` | GET | Sair da conta |

### Rotas do Chat (IA)
| Rota | Método | Descrição |
|------|--------|-----------|
| `/chat` | POST | Enviar mensagem ao assistente IA |

### Rotas Administrativas
| Rota | Método | Descrição |
|------|--------|-----------|
| `/catalogo` | GET | Painel de gerenciamento de produtos |
| `/adicionar` | POST | Criar novo produto |
| `/editar/<id>` | GET | Formulário de edição de produto |
| `/atualizar/<id>` | POST | Salvar alterações do produto |
| `/deletar/<id>` | POST | Remover produto |
| `/pedidos` | GET | Visualizar todos os pedidos (admin) |

## 💾 Estrutura do Banco de Dados

### MongoDB - Coleções

#### `usuarios_col` (Usuários)
```json
{
  "_id": ObjectId,
  "nome": "String",
  "email": "String (único)",
  "senha": "String (hash PBKDF2)",
  "criado_em": "DateTime",
  "ativo": "Boolean"
}
```

#### `produtos_col` (Produtos)
```json
{
  "_id": ObjectId,
  "nome": "String",
  "preco": "Float",
  "descricao": "String",
  "categoria": "String",
  "imagem": "String (URL)",
  "estoque": "Integer",
  "criado_em": "DateTime"
}
```

#### `pedidos_col` (Pedidos)
```json
{
  "_id": ObjectId,
  "usuario_id": ObjectId,
  "usuario_nome": "String",
  "usuario_email": "String",
  "itens": [
    {
      "produto_id": ObjectId,
      "nome": "String",
      "preco": "Float",
      "quantidade": "Integer"
    }
  ],
  "total": "Float",
  "status": "String (pending, processing, completed)",
  "data_pedido": "DateTime",
  "data_entrega": "DateTime (opcional)"
}
```

## 🔄 Fluxo de Processos

### Fluxo de Compra
```
1. Cliente faz login
   ↓
2. Navega pela loja e adiciona produtos
   ↓
3. Revisa o carrinho
   ↓
4. Finaliza o pedido
   ↓
5. Admin vê pedido no painel
```

### Fluxo de Chat IA
```
1. Cliente envia mensagem
   ↓
2. IA processa com Groq (Llama 3.3 70B)
   ↓
3. Resposta é gerada e enviada ao cliente
   ↓
4. Histórico da conversa é mantido
```

## 🤖 Integração com IA (Groq)

O assistente virtual utiliza a API Groq com o modelo **Llama 3.3 70B** para:

- ✅ Compreender perguntas sobre produtos e preços
- ✅ Fornecer recomendações personalizadas
- ✅ Detectar automaticamente intenção de compra
- ✅ Processar pedidos via chat
- ✅ Responder dúvidas sobre a loja
- ✅ Oferecer suporte em tempo real

**Modelo usado:** Llama 3.3 70B  
**Temperatura:** 0.7 (criativo mas equilibrado)  
**Max tokens:** 1024

### Como Usar o Chat IA
1. Acesse a página inicial ou `/chat`
2. Digite sua pergunta ou pedido
3. Receba resposta automática da IA

##  Segurança

### Implementações de Segurança
- ✅ **Hash de Senhas:** PBKDF2 via Werkzeug
- ✅ **Sessões:** Flask-Login com ID de usuário
- ✅ **CSRF Protection:** Token CSRF em formulários
- ✅ **SQL Injection:** Protegido via PyMongo (queries parametrizadas)
- ✅ **Validação:** Email e dados de entrada validados
- ✅ **Variáveis Sensíveis:** .env (não versionado)

### Boas Práticas
1. Nunca commite o arquivo `.env`
2. Use `https://` em produção
3. Altere `SECRET_KEY` em produção
4. Mantenha dependências atualizadas
5. Use senhas fortes (admin)
6. Revise logs regularmente

## 🧪 Testes

### Teste Manual da Loja

```bash
# 1. Inicie a aplicação
python projeto_loja.py

# 2. Acesse no navegador
http://localhost:5000

# 3. Teste fluxo:
# - Faça cadastro em /cadastro
# - Faça login com suas credenciais
# - Adicione produtos ao carrinho
# - Finalize um pedido
```

### Teste do Chat IA

```bash
# 1. Acesse http://localhost:5000/chat
# 2. Digite: "Quais são seus produtos?"
# 3. Digite: "Quero pedir 2 de arroz"
# 4. Verifique se a IA responde corretamente
```

### Teste Admin

```bash
# 1. Login com: testeadmin@gmail.com / admin123
# 2. Acesse /catalogo
# 3. Adicione um novo produto
# 4. Edite e delete para testar
# 5. Acesse /pedidos para ver todos
```

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError"
**Solução:**
```bash
pip install -r requirements.txt --upgrade
```

### Erro: "Connection refused MongoDB"
**Solução:**
- Verifique se MongoDB está rodando
- Confirme a URI em `.env`
- Para MongoDB Atlas, verifique IP whitelist

### Erro: "GROQ_KEY não definida"
**Solução:**
- Crie arquivo `.env` na raiz
- Adicione: `GROQ_KEY=sua_chave_aqui`
- Reinicie a aplicação



### Porta 5000 já em uso
**Solução:**
```bash
# Windows
netstat -ano | findstr :5000

# Linux/macOS
lsof -i :5000

# Mude a porta no código ou execute:
python projeto_loja.py --port 5001
```

## 📦 Dependências

Instale com:
```bash
pip install -r requirements.txt
```

Principais pacotes:
```
Flask==2.3.0
Flask-Login==0.6.2
pymongo==4.4.0
groq==0.5.0
python-dotenv==1.0.0
werkzeug==2.3.0
```

## 🚀 Deploy em Produção

### Opções Recomendadas

#### 1. **Heroku**
```bash
# 1. Crie Procfile
web: gunicorn projeto_loja:app

# 2. Deploy
heroku create seu-app-name
git push heroku main
```

#### 2. **PythonAnywhere**
- Upload dos arquivos
- Configure variáveis de ambiente
- Reinicie a aplicação

#### 3. **AWS/DigitalOcean/Google Cloud**
- Use Docker (Dockerfile recomendado)
- Configure com Nginx + Gunicorn
- Configure SSL/TLS

### Checklist Pré-Deploy
- [ ] Altere `FLASK_ENV=production`
- [ ] Configure `SECRET_KEY` seguro
- [ ] Mude senha admin padrão
- [ ] Use HTTPS obrigatório
- [ ] Configure CORS se necessário
- [ ] Monitore logs
- [ ] Configure backups MongoDB
- [ ] Teste todas as rotas

## 📝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes
- Mantenha o código limpo e documentado
- Adicione comentários para lógica complexa
- Teste suas mudanças antes de submeter
- Siga o padrão de código existente

## 🗂️ Roadmap

### Próximas Melhorias

- [ ] Sistema de pagamento integrado (Stripe/PayPal)
- [ ] Email de confirmação automático
- [ ] Rastreamento de pedidos em tempo real
- [ ] Avaliações e comentários de produtos
- [ ] Wishlist/Favoritos
- [ ] Desconto e cupons
- [ ] Relatórios e gráficos (admin)
- [ ] API RESTful completa
- [ ] Aplicativo mobile (Flutter)
- [ ] Testes unitários e integração
- [ ] Melhor UX/UI
- [ ] Suporte a múltiplos idiomas

## 📞 Suporte e Contato

### Informações da Loja
- **Email:** blablabla@gmail.com
- **Celular:** 85 9432-478
- **Instagram:** @Showdebola_arretado

### Suporte Técnico
- Abra uma issue no repositório
- Envie email para desenvolvimento
- Consulte a documentação

## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Juan doth**
- GitHub: [@juandoth](https://github.com/juandoth)
- Email: juandothcoelho@gmail.com

## 📊 Estatísticas do Projeto

- **Linguagem:** Python 3.8+
- **Framework:** Flask
- **Banco de Dados:** MongoDB
- **Linhas de Código:** ~2000+
- **Arquivos:** 20+
- **Status:** Em Desenvolvimento Ativo

---

**Última atualização:** Abril de 2026  
**Versão:** 1.0.0  
**Status:** 🚧 Em desenvolvimento
