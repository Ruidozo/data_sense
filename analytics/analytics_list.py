"""
Módulo que define a lista de analíticas disponíveis no Activity Provider.

Define as métricas quantitativas e qualitativas que podem ser recolhidas
durante a execução da atividade DataSense.
"""


def get_analytics_list():
    """
    Retorna a lista de analíticas (métricas) que este Activity Provider
    pode fornecer à plataforma Inven!RA.
    
    Divide-se em:
    - quantAnalytics: métricas numéricas/quantitativas
    - qualAnalytics: métricas textuais/qualitativas
    
    Returns:
        dict: Dicionário com as listas de analíticas quantitativas e qualitativas
    """
    return {
        "quantAnalytics": [
            {
                "name": "tentativas",
                "type": "integer"
            },
            {
                "name": "tempoExploracao",
                "type": "integer"
            },
            {
                "name": "graficosGerados",
                "type": "integer"
            },
            {
                "name": "taxaAcerto",
                "type": "float"
            }
        ],
        "qualAnalytics": [
            {
                "name": "reflexaoAluno",
                "type": "text/plain"
            },
            {
                "name": "tipoErro",
                "type": "text/plain"
            }
        ]
    }
