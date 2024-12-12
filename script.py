import pandas as pd
import random
import uuid
import os


##################################################
# Script para combinações numeros Mega da Virada #
##################################################

arquivo = 'origem.xlsx'

if not os.path.exists(arquivo):
    print(f"Arquivo '{arquivo}' não encontrado na pasta do script!")
else:
    print(f"Arquivo '{arquivo}' encontrado. Processando...")

df = pd.read_excel(arquivo)

colunas_numeros = df.columns[1:7]

jogos_existentes = df[colunas_numeros].apply(lambda row: set(row), axis=1).tolist()
jogos_existentes_set = set(map(frozenset, jogos_existentes))

numeros = df[colunas_numeros].values.flatten()
frequencias = pd.Series(numeros).value_counts()

top_numeros = list(frequencias.index[:15])
bottom_numeros = list(frequencias.index[-15:])

novos_jogos = []
while len(novos_jogos) < 300:
    combinacao_top = random.sample(top_numeros, 3)
    combinacao_bottom = random.sample(bottom_numeros, 3)
    combinacao = sorted(combinacao_top + combinacao_bottom)
    jogo_set = frozenset(combinacao)
    if jogo_set not in jogos_existentes_set:
        novos_jogos.append(combinacao)
        jogos_existentes_set.add(jogo_set)

novos_jogos_df = pd.DataFrame(novos_jogos, columns=[f"Número {i + 1}" for i in range(6)])
nome_arquivo = f"novos_jogos_{uuid.uuid4().hex[:8]}.xlsx"
novos_jogos_df.to_excel(nome_arquivo, index=False)

print(f"300 combinações exclusivas foram geradas e salvas em '{nome_arquivo}'.")
