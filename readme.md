# 🤖 LLM API - Sistema de Gerenciamento de Modelos

Uma API REST desenvolvida em FastAPI para gerenciar modelos de linguagem (LLM) seguindo o padrão arquitetural MVC.

## 📋 Índice

- [Características](#-características)
- [Tecnologias](#-tecnologias)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Uso](#-uso)
- [Endpoints](#-endpoints)
- [Exemplos](#-exemplos)
- [Estrutura do Projeto](#-estrutura-do-projeto)

## ✨ Características

- **CRUD Completo** para modelos LLM
- **Suporte a múltiplos tipos** de modelos (OpenAI, Anthropic, etc.)
- **Validação robusta** com Pydantic
- **Banco de dados MySQL** com SQLAlchemy
- **Documentação automática** com Swagger/OpenAPI
- **Arquitetura MVC** limpa e organizada

## 🛠 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para Python
- **MySQL** - Banco de dados relacional
- **Pydantic** - Validação de dados
- **Uvicorn** - Servidor ASGI

## 🚀 Instalação

### Pré-requisitos

- Python 3.8+
- MySQL 8.0+
- pip (gerenciador de pacotes Python)

### Passos

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/llm-api.git
   cd llm-api
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuração

1. **Crie o arquivo `.env`** na raiz do projeto:
   ```env
   DATABASE_URL=mysql+pymysql://root:sua_senha@localhost:3306/llm_api?charset=utf8mb4
   OPENAI_API_KEY=sua_chave_openai_aqui
   ```

2. **Crie o banco de dados MySQL**:
   ```sql
   CREATE DATABASE llm_api CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```

3. **Execute a aplicação**:
   ```bash
   python main.py
   ```

A API estará disponível em: `http://localhost:8000`

## 📖 Uso

### Documentação Interativa

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Estrutura de Resposta

Todas as respostas seguem o padrão JSON com os seguintes campos principais:

```json
{
  "id": 1,
  "name": "GPT-3.5 Turbo",
  "model_type": "openai",
  "model_name": "gpt-3.5-turbo",
  "temperature": "0.7",
  "max_tokens": 1000,
  "description": "Modelo para conversação geral",
  "is_active": true,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": null
}
```

## 🔗 Endpoints

### Modelos LLM

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST   | `/api/llm-models/` | Criar novo modelo |
| GET    | `/api/llm-models/` | Listar todos os modelos |
| GET    | `/api/llm-models/{id}` | Buscar modelo por ID |
| PUT    | `/api/llm-models/{id}` | Atualizar modelo |
| DELETE | `/api/llm-models/{id}` | Deletar modelo |

## 💡 Exemplos

### Criar um Modelo

```bash
curl -X POST "http://localhost:8000/api/llm-models/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "GPT-3.5 Turbo",
    "model_type": "openai",
    "model_name": "gpt-3.5-turbo",
    "api_key": "sk-sua-chave-aqui",
    "temperature": "0.7",
    "max_tokens": 1000,
    "description": "Modelo para conversação geral",
    "is_active": true
  }'
```

### Listar Modelos

```bash
curl -X GET "http://localhost:8000/api/llm-models/"
```

### Atualizar Modelo

```bash
curl -X PUT "http://localhost:8000/api/llm-models/1" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": "0.8",
    "max_tokens": 1500
  }'
```

### Deletar Modelo

```bash
curl -X DELETE "http://localhost:8000/api/llm-models/1"
```

## 📁 Estrutura do Projeto

```
llm-api/
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências Python
├── .env                   # Variáveis de ambiente (não commitado)
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Documentação do projeto
├── config/
│   └── database.py       # Configuração do banco de dados
├── models/
│   └── llm_model.py      # Modelo SQLAlchemy
├── schemas/
│   └── llm_schema.py     # Schemas Pydantic
├── services/
│   └── llm_service.py    # Lógica de negócio
└── controllers/
    └── llm_controller.py # Controladores das rotas
```

## 🔧 Campos do Modelo

### Campos Obrigatórios
- `name`: Nome do modelo (string, 1-255 caracteres)
- `model_type`: Tipo do modelo (string, ex: "openai", "anthropic")
- `model_name`: Nome específico do modelo (string, ex: "gpt-3.5-turbo")

### Campos Opcionais
- `api_key`: Chave da API (string, opcional)
- `temperature`: Temperatura do modelo (string, padrão: "0.7")
- `max_tokens`: Máximo de tokens (integer, padrão: 1000, máx: 4000)
- `description`: Descrição do modelo (string, opcional)
- `is_active`: Status ativo (boolean, padrão: true)

### Campos Automáticos
- `id`: Identificador único (auto-incremento)
- `created_at`: Data de criação (timestamp automático)
- `updated_at`: Data de atualização (timestamp automático)

## 🔍 Códigos de Status HTTP

| Código | Descrição |
|--------|-----------|
| 200    | Sucesso |
| 201    | Criado com sucesso |
| 204    | Deletado com sucesso |
| 400    | Erro de validação |
| 404    | Recurso não encontrado |
| 422    | Erro de validação Pydantic |
| 500    | Erro interno do servidor |

## 🛡️ Validações

### Criação de Modelo
- Nome não pode ser vazio
- Tipo de modelo é obrigatório
- Nome do modelo é obrigatório
- Max tokens deve estar entre 1 e 4000

## 🔄 Paginação

Os endpoints de listagem suportam paginação:

```bash
GET /api/llm-models/?skip=0&limit=10
```

- `skip`: Número de registros para pular (padrão: 0)
- `limit`: Número máximo de registros (padrão: 100)

## 🐛 Solução de Problemas

### Erro de Conexão com MySQL
```
RuntimeError: 'cryptography' package is required
```
**Solução**: `pip install cryptography`

**Solução**: Verifique as credenciais no arquivo `.env`

### Modelo não encontrado
```
404 Not Found
```
**Solução**: Verifique se o ID do modelo existe no banco
