"""
Padrão Factory Method - Interface abstrata para geradores de gráficos.

Este módulo implementa o padrão de criação Factory Method para criar
diferentes tipos de visualizações de dados (gráficos).
"""

from abc import ABC, abstractmethod
from datetime import datetime


class ChartGenerator(ABC):
    """
    Interface abstrata para geradores de gráficos.
    Define o contrato que todas as implementações concretas devem seguir.
    """
    
    @abstractmethod
    def generate(self, data: dict) -> dict:
        """
        Método abstrato para gerar um gráfico.
        
        Args:
            data: Dados para gerar o gráfico
            
        Returns:
            dict: Metadados do gráfico gerado
        """
        pass
    
    @abstractmethod
    def get_type(self) -> str:
        """Retorna o tipo de gráfico."""
        pass


class BarChartGenerator(ChartGenerator):
    """Gerador concreto de gráficos de barras."""
    
    def generate(self, data: dict) -> dict:
        """Gera um gráfico de barras."""
        return {
            "type": "bar",
            "timestamp": datetime.now().isoformat(),
            "config": {
                "categories": data.get("categories", []),
                "values": data.get("values", []),
                "title": data.get("title", "Gráfico de Barras"),
                "orientation": data.get("orientation", "vertical")
            },
            "status": "generated"
        }
    
    def get_type(self) -> str:
        return "bar"


class LineChartGenerator(ChartGenerator):
    """Gerador concreto de gráficos de linhas."""
    
    def generate(self, data: dict) -> dict:
        """Gera um gráfico de linhas."""
        return {
            "type": "line",
            "timestamp": datetime.now().isoformat(),
            "config": {
                "x_axis": data.get("x_axis", []),
                "y_axis": data.get("y_axis", []),
                "title": data.get("title", "Gráfico de Linhas"),
                "smooth": data.get("smooth", True)
            },
            "status": "generated"
        }
    
    def get_type(self) -> str:
        return "line"


class PieChartGenerator(ChartGenerator):
    """Gerador concreto de gráficos de pizza."""
    
    def generate(self, data: dict) -> dict:
        """Gera um gráfico de pizza."""
        return {
            "type": "pie",
            "timestamp": datetime.now().isoformat(),
            "config": {
                "labels": data.get("labels", []),
                "values": data.get("values", []),
                "title": data.get("title", "Gráfico de Pizza"),
                "show_percentage": data.get("show_percentage", True)
            },
            "status": "generated"
        }
    
    def get_type(self) -> str:
        return "pie"


class ScatterChartGenerator(ChartGenerator):
    """Gerador concreto de gráficos de dispersão."""
    
    def generate(self, data: dict) -> dict:
        """Gera um gráfico de dispersão."""
        return {
            "type": "scatter",
            "timestamp": datetime.now().isoformat(),
            "config": {
                "points": data.get("points", []),
                "title": data.get("title", "Gráfico de Dispersão"),
                "x_label": data.get("x_label", "X"),
                "y_label": data.get("y_label", "Y")
            },
            "status": "generated"
        }
    
    def get_type(self) -> str:
        return "scatter"
