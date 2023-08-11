# Projeto Santander Coders 2023 - DS

Projeto: Simulação de Jogo de Dados

Professor: Matheus Barão Fiorin

## Objetivo

Você tem a tarefa de criar uma simulação para um jogo de dados. Essa simulação tem como objetivo reunir estatísticas para analisar a justiça do jogo, possíveis resultados e fazer previsões sobre jogos futuros.

## Desafios do Projeto

Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados (valores de 1 a 6). Esta função deve retornar a soma dos resultados dos dados.

Múltiplas Simulações: Use a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos). Armazene o resultado de cada jogo em um array NumPy.

Análise de Dados: Agora, vamos analisar os resultados desses jogos. Calcule e imprima o seguinte:

- A média dos resultados.
- O lançamento máximo e mínimo.
- O número de vezes que cada possível lançamento (2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12) ocorreu.
- Teste de Hipótese: Agora vamos fazer um pouco de teste de hipóteses:
    1. Supondo um jogo justo (ou seja, todos os lançamentos são igualmente prováveis), o resultado da sua simulação coincide com essa suposição? Por que sim ou por que não?
    2. O que isso significa para um jogador do jogo de dados?

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências necessárias.

> pip install -r requirements.txt

## Uso

> python3 main.py


