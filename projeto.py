import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados 
# (valores de 1 a 6). Esta função deve retornar a soma dos resultados dos dados.

soma_lancamento_dados = lambda numero_de_dados: np.sum(np.random.choice(np.arange(1,7, dtype='int64'), \
                                                                        numero_de_dados, replace=True))


# Múltiplas Simulações: Use a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos).
# Armazene o resultado de cada jogo em um array NumPy.

simular_lancamentos = lambda numero_de_lancamentos, funcao_gerar_soma, numero_de_dados: np.array([funcao_gerar_soma(numero_de_dados) \
                                                                               for _ in range(numero_de_lancamentos)])

# Análise de Dados: Agora, vamos analisar os resultados desses jogos. Calcule e imprima o seguinte:

# A média dos resultados.
# O lançamento máximo e mínimo.

def calcular_medidas_de_posicao(arr, **kwargs) -> dict:
    return {k: v(arr) for k, v in kwargs.items()}
        

# O número de vezes que cada possível lançamento (2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12) ocorreu.

def contar_valores(arr:np.array) -> dict:
    value, counts = np.unique(arr, return_counts=True)

    return {item[0]: item[1] for item in zip(value, counts)}

# Teste de Hipótese: Agora vamos fazer um pouco de teste de hipóteses:
# Supondo um jogo justo (ou seja, todos os lançamentos são igualmente prováveis), 
# o resultado da sua simulação coincide com essa suposição? Por que sim ou por que não?
# O que isso significa para um jogador do jogo de dados?

def plotar_histograma(arr:np.array, eixo_x_titulo:str=None, 
                      eixo_y_titulo:str=None,
                      medidas_de_posicao:dict=None,
                      **kwargs) -> None:
    
    
    sns.displot(arr, discrete=True)
    sns.despine()
    
    if eixo_x_titulo is not None:plt.xlabel(eixo_x_titulo)
    if eixo_y_titulo is not None:plt.ylabel(eixo_y_titulo)

    # Maximo valor (frequencia)
    _, frequencia = np.unique(arr, return_counts=True)
    maximo = frequencia.max()

    
    if medidas_de_posicao is not None:
        for k in kwargs:
            if k in medidas_de_posicao:
                plt.vlines(medidas_de_posicao[k], ymin=0, ymax=maximo*1.1,
                           colors=kwargs[k][0],
                           linestyles=kwargs[k][1],
                           label=k)
        plt.legend()
    
    plt.show()

if __name__ == '__main__':
    NUMERO_DE_DADOS = 2
    NUMERO_DE_LANCAMENTOS = 1000

    # Reproducibilidade -> Optional
    np.random.seed(40)

    simulacao = simular_lancamentos(NUMERO_DE_LANCAMENTOS, soma_lancamento_dados, NUMERO_DE_DADOS)

    medidas_de_posicao = calcular_medidas_de_posicao(simulacao, media=np.mean, minimo=np.min, maximo=np.max)

    print(f'As medidas de posição são:\n {pd.Series(medidas_de_posicao)}')

    print(f'Frequência absoluta dos resultados:\n{pd.Series(contar_valores(simulacao))}')

    plotar_histograma(simulacao, 'Valores unicos', 'Frequencia', 
                      medidas_de_posicao=medidas_de_posicao, 
                      media=['grey', 'dotted'],
                      minimo=['red', 'dashed'],
                      maximo=['green', 'dashed'])
