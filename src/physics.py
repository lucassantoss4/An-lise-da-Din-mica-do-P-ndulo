import numpy as np
from scipy.integrate import odeint
from math import sqrt, pi

class PendulumSimulator:
    """
    Classe para simular a dinâmica de um pêndulo simples com força de arrasto.
    """
    def __init__(self, g=9.8, rho=1.225, cd=0.47):
        """
        Inicializa os parâmetros constantes.
        :param g: Aceleração da gravidade (m/s^2)
        :param rho: Densidade do ar (kg/m^3)
        :param cd: Coeficiente de arrasto
        """
        self.g = g
        self.rho = rho
        self.cd = cd

    def _model(self, state, t, l, m, r):
        """
        Equações diferenciais do pêndulo.
        """
        x, y, vx, vy = state
        v = sqrt(vx**2 + vy**2)
        
        # Geometria do pêndulo
        sin_theta = x / l
        cos_theta = -y / l
        
        # Área da seção transversal
        area = pi * (r**2)
        
        # Força de arrasto
        fa = self.rho * area * self.cd * (v**2) * 0.5
        
        # Componentes da velocidade para direção do arrasto
        if v > 0:
            cos_alpha = vx / v
            sin_alpha = vy / v
        else:
            cos_alpha = sin_alpha = 0
            
        # Tração no fio
        traction = m * v**2 / l + m * self.g * cos_theta
        
        # Derivadas
        dxdt = vx
        dydt = vy
        dvxdt = (-traction * sin_theta - fa * cos_alpha) / m
        dvydt = (traction * cos_theta - fa * sin_alpha) / m - self.g
        
        return [dxdt, dydt, dvxdt, dvydt]

    def simulate(self, l, m, r, initial_conditions, t_array):
        """
        Executa a simulação para um conjunto de parâmetros.
        """
        return odeint(self._model, initial_conditions, t_array, args=(l, m, r))

    def calculate_period(self, y_values, t_values):
        """
        Calcula o período baseado no primeiro pico de altura máxima (y).
        """
        for i in range(1, len(y_values) - 1):
            if y_values[i] > y_values[i-1] and y_values[i] > y_values[i+1]:
                return t_values[i]
        return None

    def calculate_max_height(self, y_values):
        """
        Calcula a altura máxima (pico) atingida.
        """
        for i in range(1, len(y_values) - 1):
            if y_values[i] > y_values[i-1] and y_values[i] > y_values[i+1]:
                return y_values[i]
        return None
