# DataSense Activity Provider

Activity Provider para a arquitetura Inven!RA.

## Descrição

Implementação de um Activity Provider (AP) compatível com a arquitetura Inven!RA, com 5 endpoints REST obrigatórios.

## Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/config` | Página de configuração |
| GET | `/json-params` | Parâmetros configuráveis |
| POST | `/user` | Estado da atividade |
| GET | `/analytics-list` | Lista de analíticas |
| POST | `/analytics` | Recepção de analíticas |

## Instalação

```bash
cd datasense_ap
pip install -r requirements.txt
python app.py
```

Servidor disponível em `http://localhost:8080`

## Testar

```bash
curl http://localhost:8080/
curl http://localhost:8080/json-params
curl http://localhost:8080/analytics-list
```


## Tecnologias

- Flask 3.0.0
- Flask-Cors 4.0.0
- Gunicorn 21.2.0
- Python 3.11+

---

Projeto académico - Mestrado em Engenharia Informática - Universidade Aberta
