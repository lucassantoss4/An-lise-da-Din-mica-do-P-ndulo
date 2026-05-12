# 🏮 Análise da Dinâmica do Pêndulo de Ondas

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Scipy](https://img.shields.io/badge/Scipy-1.10+-green.svg)](https://scipy.org/)
[![Status](https://img.shields.io/badge/Status-Portfolio--Ready-brightgreen.svg)]()

Este projeto apresenta uma análise técnica profunda sobre a dinâmica de oscilação de pêndulos simples, integrando modelagem matemática clássica com validação experimental baseada em dados reais.

## 📌 Contexto
O projeto investiga o fenômeno do **Pêndulo de Ondas**, onde múltiplos pêndulos de comprimentos variados são soltos simultaneamente, criando padrões visuais complexos devido às diferenças em seus períodos de oscilação.

### Destaques Técnicos:
- **Modelagem Numérica:** Resolução de Equações Diferenciais Ordinárias (ODEs) utilizando `scipy.integrate.odeint`.
- **Física do Mundo Real:** Inclusão de forças dissipativas (arrasto do ar) para maior precisão.
- **Validação:** Comparação de dados simulados com dados experimentais extraídos via software Tracker.
- **Engenharia de Software:** Código modularizado em classes e pacotes Python.

## 📂 Estrutura do Projeto
```text
├── data/               # Dados experimentais (CSV)
├── notebooks/          # Análises e visualizações (Jupyter Notebook)
├── src/                # Motor de simulação física e utilitários
├── video pendulo.mp4   # Vídeo original do experimento
├── requirements.txt    # Dependências para reprodução
└── README.md
```

## 🛠️ Como Executar
1. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   # No Windows: .\.venv\Scripts\activate
   # No Linux/Mac: source .venv/bin/activate
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Explore a análise completa no notebook (certifique-se de configurar o Kernel do Jupyter para o ambiente virtual recém-criado):
   `notebooks/pendulum_analysis.ipynb`

## 📊 Resultados Principais
O modelo demonstrou que a inclusão do coeficiente de arrasto ($C_d = 0.47$) foi crucial para validar a perda de energia observada no experimento real, permitindo prever com precisão o comportamento do sistema ao longo do tempo.

---
**Desenvolvido por Lucas Santos**  
*Insper - Instituto de Ensino e Pesquisa*
