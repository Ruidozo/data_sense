"""
Módulo de armazenamento de analíticas recebidas.

Recebe e armazena as analíticas enviadas pela plataforma Inven!RA.
Em produção, seria persistido numa base de dados.
Nesta versão mock, mantemos os dados em memória.
"""

from datetime import datetime

# Armazenamento em memória das analíticas recebidas
analytics_data = []


def store_analytics(analytics_payload):
    """
    Armazena os dados de analíticas recebidos da plataforma Inven!RA.
    
    Args:
        analytics_payload (dict): Dados de analíticas enviados pela plataforma
    
    Returns:
        dict: Confirmação de recepção
    """
    # Adiciona timestamp de recepção
    entry = {
        "timestamp": datetime.now().isoformat(),
        "data": analytics_payload
    }
    
    analytics_data.append(entry)
    
    return {
        "status": "analytics received",
        "total_entries": len(analytics_data)
    }


def get_all_analytics():
    """
    Retorna todas as analíticas armazenadas.
    Útil para consulta e debug.
    
    Returns:
        list: Lista de todas as entradas de analíticas
    """
    return analytics_data


def clear_analytics():
    """
    Limpa todos os dados de analíticas armazenados.
    Útil para testes e reset.
    """
    global analytics_data
    analytics_data = []
    return {"status": "analytics cleared"}
