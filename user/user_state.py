"""
Módulo de gestão do estado do utilizador.

Este módulo é responsável por gerir o estado da atividade para cada utilizador.
Em produção, o estado seria persistido numa base de dados.
Nesta versão mock, mantemos os dados em memória.
"""

from charts import ChartFactoryRegistry

# Armazenamento em memória do estado dos utilizadores
# Formato: {(activityId, userId): {...estado...}}
user_states = {}

# Armazenamento de gráficos gerados por utilizador
user_charts = {}


def get_user_state(activity_id, user_id):
    """
    Obtém ou cria o estado da atividade para um utilizador específico.

    Args:
        activity_id (str): Identificador da atividade
        user_id (str): Identificador do utilizador

    Returns:
        dict: Resposta com o estado do utilizador
    """
    key = (activity_id, user_id)

    # Se o utilizador ainda não tem estado, inicializa
    if key not in user_states:
        user_states[key] = {
            "graficosGerados": 0,
            "tentativas": 0,
            "progresso": "iniciado",
            "tiposGraficos": []
        }
        user_charts[key] = []

    return {
        "status": "ok",
        "message": "Atividade iniciada",
        "userState": user_states[key]
    }


def update_user_state(activity_id, user_id, state_updates):
    """
    Atualiza o estado de um utilizador.

    Args:
        activity_id (str): Identificador da atividade
        user_id (str): Identificador do utilizador
        state_updates (dict): Campos a atualizar no estado

    Returns:
        dict: Estado atualizado
    """
    key = (activity_id, user_id)

    if key not in user_states:
        user_states[key] = {
            "graficosGerados": 0,
            "tentativas": 0,
            "progresso": "iniciado",
            "tiposGraficos": []
        }

    # Atualiza os campos fornecidos
    user_states[key].update(state_updates)

    return user_states[key]


def generate_chart_for_user(activity_id, user_id, chart_type, data):
    """
    Gera um gráfico para o utilizador usando o padrão Factory Method.

    Args:
        activity_id (str): ID da atividade
        user_id (str): ID do utilizador
        chart_type (str): Tipo de gráfico ("bar", "line", "pie", "scatter")
        data (dict): Dados para gerar o gráfico

    Returns:
        dict: Informações do gráfico gerado
    """
    key = (activity_id, user_id)

    # Obter a factory registry (Singleton)
    registry = ChartFactoryRegistry()

    try:
        # Obter a factory apropriada
        factory = registry.get_factory(chart_type)

        # Gerar o gráfico usando a factory
        chart = factory.generate_chart(data)

        # Armazenar o gráfico gerado
        if key not in user_charts:
            user_charts[key] = []
        user_charts[key].append(chart)

        # Atualizar estado do utilizador
        if key not in user_states:
            get_user_state(activity_id, user_id)

        user_states[key]["graficosGerados"] += 1
        if chart_type not in user_states[key]["tiposGraficos"]:
            user_states[key]["tiposGraficos"].append(chart_type)

        return {
            "status": "success",
            "chart": chart,
            "totalCharts": user_states[key]["graficosGerados"]
        }

    except ValueError as e:
        return {
            "status": "error",
            "message": str(e),
            "availableTypes": registry.get_available_types()
        }


def get_user_charts(activity_id, user_id):
    """
    Retorna todos os gráficos gerados por um utilizador.

    Args:
        activity_id (str): ID da atividade
        user_id (str): ID do utilizador

    Returns:
        list: Lista de gráficos gerados
    """
    key = (activity_id, user_id)
    return user_charts.get(key, [])
