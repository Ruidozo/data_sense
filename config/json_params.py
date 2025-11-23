"""
Módulo de parâmetros configuráveis do Activity Provider DataSense.

Este módulo define os parâmetros que podem ser configurados pela plataforma
Inven!RA ao integrar este Activity Provider.
"""


def get_json_params():
    """
    Retorna a lista de parâmetros configuráveis do Activity Provider.
    
    Cada parâmetro tem:
    - name: nome identificador do parâmetro
    - type: tipo de dado esperado (text/plain, URL, integer, etc.)
    
    Returns:
        list: Lista de dicionários com os parâmetros configuráveis
    """
    return [
        {
            "name": "tema",
            "type": "text/plain"
        },
        {
            "name": "fonteDados",
            "type": "URL"
        },
        {
            "name": "objetivoAnalitico",
            "type": "text/plain"
        },
        {
            "name": "nivelDificuldade",
            "type": "integer"
        },
        {
            "name": "tipoDesafio",
            "type": "text/plain"
        },
        {
            "name": "tempoMaximo",
            "type": "integer"
        }
    ]
