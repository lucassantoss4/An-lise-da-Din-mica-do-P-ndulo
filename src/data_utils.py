import pandas as pd

def load_experimental_data(filepath):
    """
    Carrega e limpa os dados experimentais do Tracker.
    """
    colunas = ['t', 'x', 'y', 'vx', 'vy']
    try:
        dados = pd.read_csv(filepath, names=colunas)
        
        # Ajustes de medida identificados no experimento original
        t0 = dados['t'].iloc[0]
        dados['t'] = dados['t'] - t0
        dados['y'] = dados['y'] + 0.02
        
        return dados
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def get_simulation_parameters():
    """
    Retorna os parâmetros padrão do experimento.
    """
    return {
        'm': 0.01122,  # massa (kg)
        'r': 0.007,    # raio (m)
        'rho': 1.25,   # densidade do ar (kg/m^3)
        'g': 9.80      # gravidade (m/s^2)
    }
