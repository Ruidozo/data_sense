"""
Padrão Factory Method - Factories para criação de geradores de gráficos.

Este módulo implementa o padrão Factory Method através de uma classe Factory
que cria instâncias dos diferentes tipos de geradores de gráficos.
"""

from abc import ABC, abstractmethod

from .chart_generator import (BarChartGenerator, ChartGenerator,
                              LineChartGenerator, PieChartGenerator,
                              ScatterChartGenerator)


class ChartFactory(ABC):
    """
    Factory abstrata para criação de geradores de gráficos.
    Implementa o padrão Factory Method.
    """
    
    @abstractmethod
    def create_chart_generator(self) -> ChartGenerator:
        """
        Factory Method: cria um gerador de gráficos.
        Cada subclasse concreta implementa este método para criar
        o tipo específico de gerador.
        """
        pass
    
    def generate_chart(self, data: dict) -> dict:
        """
        Operação que usa o Factory Method.
        Cria o gerador e usa-o para gerar o gráfico.
        """
        generator = self.create_chart_generator()
        return generator.generate(data)


class BarChartFactory(ChartFactory):
    """Factory concreta para gráficos de barras."""
    
    def create_chart_generator(self) -> ChartGenerator:
        return BarChartGenerator()


class LineChartFactory(ChartFactory):
    """Factory concreta para gráficos de linhas."""
    
    def create_chart_generator(self) -> ChartGenerator:
        return LineChartGenerator()


class PieChartFactory(ChartFactory):
    """Factory concreta para gráficos de pizza."""
    
    def create_chart_generator(self) -> ChartGenerator:
        return PieChartGenerator()


class ScatterChartFactory(ChartFactory):
    """Factory concreta para gráficos de dispersão."""
    
    def create_chart_generator(self) -> ChartGenerator:
        return ScatterChartGenerator()


# Singleton para gerenciar as factories disponíveis
class ChartFactoryRegistry:
    """
    Registry (Singleton) que mantém todas as factories disponíveis.
    Permite obter a factory correta baseado no tipo de gráfico.
    """
    
    _instance = None
    _factories = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_factories()
        return cls._instance
    
    def _initialize_factories(self):
        """Regista todas as factories disponíveis."""
        self._factories = {
            "bar": BarChartFactory(),
            "line": LineChartFactory(),
            "pie": PieChartFactory(),
            "scatter": ScatterChartFactory()
        }
    
    def get_factory(self, chart_type: str) -> ChartFactory:
        """
        Obtém a factory apropriada para o tipo de gráfico.
        
        Args:
            chart_type: Tipo de gráfico ("bar", "line", "pie", "scatter")
            
        Returns:
            ChartFactory correspondente
            
        Raises:
            ValueError: Se o tipo não for suportado
        """
        factory = self._factories.get(chart_type.lower())
        if factory is None:
            raise ValueError(f"Tipo de gráfico '{chart_type}' não suportado")
        return factory
    
    def get_available_types(self) -> list:
        """Retorna lista de tipos de gráficos disponíveis."""
        return list(self._factories.keys())
