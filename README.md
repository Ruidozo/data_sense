# 🎯 DataSense Activity Provider

Activity Provider para a arquitetura **Inven!RA**, desenvolvido para análise e visualização de dados educacionais.

## 📋 Descrição

Este projeto implementa a **Fase 1** de um Activity Provider (AP) compatível com a arquitetura Inven!RA, oferecendo os 5 endpoints REST obrigatórios com dados de exemplo (mock).

### Endpoints Implementados

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/config` | Página HTML de confirmação de configuração |
| GET | `/json-params` | Parâmetros configuráveis do AP |
| POST | `/user` | Estado da atividade para um utilizador |
| GET | `/analytics-list` | Lista de analíticas disponíveis |
| POST | `/analytics` | Recepção de dados de analíticas |

## 🗂️ Estrutura do Projeto

```
datasense_ap/
│
├── app.py                      # Servidor Flask principal
├── config/
│   └── json_params.py          # Parâmetros configuráveis
├── analytics/
│   ├── analytics_list.py       # Lista de métricas disponíveis
│   └── analytics_store.py      # Armazenamento de analíticas
├── user/
│   └── user_state.py           # Gestão do estado do utilizador
├── static/
│   └── config.html             # Página de configuração
├── requirements.txt            # Dependências Python
└── README.md                   # Este ficheiro
```

## 🚀 Instalação e Execução Local

### Pré-requisitos

- Python 3.8 ou superior
- pip (gestor de pacotes Python)

### Passos de Instalação

1. **Clone ou navegue até o diretório do projeto:**
   ```bash
   cd datasense_ap
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv venv
   ```

3. **Ative o ambiente virtual:**
   ```bash
   # macOS/Linux:
   source venv/bin/activate
   
   # Windows:
   venv\Scripts\activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute o servidor Flask:**
   ```bash
   flask --app app run --host=0.0.0.0 --port=8080
   ```

   Ou alternativamente:
   ```bash
   python app.py
   ```
   
   > **Nota:** Se a porta 5000 estiver ocupada (comum no macOS pelo AirPlay Receiver), o servidor usará automaticamente a porta 8080.

6. **O servidor estará disponível em:**
   ```
   http://localhost:8080
   ```
   
   (ou `http://localhost:5000` se a porta 5000 estiver livre)

## 🧪 Testar os Endpoints

### 1. Testar a raiz (informações do AP)
```bash
curl http://localhost:8080/
```

### 2. Testar página de configuração
```bash
curl http://localhost:8080/config
```
Ou abra no navegador: `http://localhost:8080/config`

### 3. Obter parâmetros configuráveis
```bash
curl http://localhost:8080/json-params
```

**Resposta esperada:**
```json
[
  {"name": "tema", "type": "text/plain"},
  {"name": "fonteDados", "type": "URL"},
  {"name": "objetivoAnalitico", "type": "text/plain"},
  {"name": "nivelDificuldade", "type": "integer"},
  {"name": "tipoDesafio", "type": "text/plain"},
  {"name": "tempoMaximo", "type": "integer"}
]
```

### 4. Obter estado do utilizador
```bash
curl -X POST http://localhost:8080/user \
  -H "Content-Type: application/json" \
  -d '{"activityId": "act123", "userId": "user456"}'
```

**Resposta esperada:**
```json
{
  "status": "ok",
  "message": "Atividade iniciada",
  "userState": {
    "graficosGerados": 0,
    "tentativas": 0,
    "progresso": "iniciado"
  }
}
```

### 5. Obter lista de analíticas
```bash
curl http://localhost:8080/analytics-list
```

**Resposta esperada:**
```json
{
  "quantAnalytics": [
    {"name": "tentativas", "type": "integer"},
    {"name": "tempoExploracao", "type": "integer"},
    {"name": "graficosGerados", "type": "integer"},
    {"name": "taxaAcerto", "type": "float"}
  ],
  "qualAnalytics": [
    {"name": "reflexaoAluno", "type": "text/plain"},
    {"name": "tipoErro", "type": "text/plain"}
  ]
}
```

### 6. Enviar analíticas
```bash
curl -X POST http://localhost:8080/analytics \
  -H "Content-Type: application/json" \
  -d '{
    "activityId": "act123",
    "userId": "user456",
    "tentativas": 5,
    "graficosGerados": 3,
    "taxaAcerto": 0.8
  }'
```

**Resposta esperada:**
```json
{
  "status": "analytics received",
  "total_entries": 1
}
```

## 📦 Deploy em Produção

### Opção 1: Railway

1. Crie uma conta em [Railway.app](https://railway.app)
2. Instale o Railway CLI:
   ```bash
   npm i -g @railway/cli
   ```
3. Faça login:
   ```bash
   railway login
   ```
4. No diretório do projeto:
   ```bash
   railway init
   railway up
   ```
5. Configure a variável de ambiente `PORT` (Railway define automaticamente)

### Opção 2: Render

1. Crie uma conta em [Render.com](https://render.com)
2. Faça push do código para um repositório Git (GitHub, GitLab)
3. No Render Dashboard:
   - Clique em "New +" → "Web Service"
   - Conecte o seu repositório
   - Configure:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
4. Adicione `gunicorn` ao `requirements.txt`:
   ```
   Flask==3.0.0
   Flask-Cors==4.0.0
   gunicorn==21.2.0
   ```

### Opção 3: Heroku

1. Instale o Heroku CLI
2. Crie um ficheiro `Procfile` na raiz do projeto:
   ```
   web: gunicorn app:app
   ```
3. Execute:
   ```bash
   heroku login
   heroku create datasense-ap
   git push heroku main
   ```

## 🔧 Tecnologias Utilizadas

- **Flask 3.0.0** - Framework web Python
- **Flask-Cors 4.0.0** - Habilitação de CORS
- **Python 3.8+** - Linguagem de programação

## 📝 Notas de Desenvolvimento

- Esta é a **Fase 1** do projeto - endpoints com dados mock
- Os dados são armazenados **em memória** (não persistentes)
- CORS está **ativado** para permitir integração com Inven!RA
- Para produção, considere:
  - Usar uma base de dados (PostgreSQL, MongoDB)
  - Implementar autenticação/autorização
  - Adicionar logging estruturado
  - Implementar rate limiting
  - Usar um servidor WSGI (gunicorn, uwsgi)

## 🎯 Próximas Fases

- **Fase 2:** Implementar o endpoint "provide activity"
- **Fase 3:** Integração com base de dados real
- **Fase 4:** Interface web para gestão de atividades
- **Fase 5:** Implementação de lógica real de análise de dados

## 📄 Licença

Projeto académico desenvolvido no âmbito do Mestrado em Engenharia Informática - Universidade Aberta.

## 👨‍💻 Autor

DataSense Team - 2025

---

**Versão:** 1.0.0  
**Data:** 22 de Novembro de 2025  
**Status:** ✅ Fase 1 Completa
# data_sense
