import pandas as pd
import os
import sys

from unidecode import unidecode
import re

from modules import mapBase as mb
import modules.mapBase as mb


listaArqruivos = mb.printLocalFiles('../docs/financeiro')
listaArqruivos = mb.allFiles('../docs/financeiro')

pd_financeiro = pd.read_excel(fr'../docs/financeiro/{listaArqruivos[0]}')
#pd_financeiro_santa_rosa = pd.read_excel(fr'docs/financeiro/{listaArqruivos[0]}')
#pd_financeiro_trevo = pd.read_excel(fr'docs/financeiro/{listaArqruivos[1]}')


#Trazer valores unicos de uma coluna
# =============================================================================
plano_de_contas = pd_financeiro['Plano de contas'].unique()
# #Ordenar a coluna
# plano_de_contas = pd_financeiro['Plano de contas']
# # =============================================================================
plano_de_contas = sorted(plano_de_contas)
#Remover Duplicadas
#plano_de_contas = plano_de_contas.drop_duplicates()

#crio um dicionario vazio para atribuir a chave do plano de conta nele
plano = {}
#faço um for para atribuir a cada chave um dataframe filtrado com o nome da coluna
for i in plano_de_contas:
    plano[i] = pd_financeiro[pd_financeiro['Plano de contas'] == i]

#vou unir pelas chaves do dicionario os dois arquivos que são de recebimentos da loja
df_recebidos =pd.concat([plano['Vendas de produtos'],plano['Vendas no balcão']])

#tratamento das colunas
def tratamento_coluna_str (df,coluna):
    df[coluna] = df[coluna].astype('str')
    df[coluna] = df[coluna].apply(lambda x: unidecode(x))
    df[coluna] = df[coluna].apply(lambda x: re.sub('[^A-Za-z0-9]+', ' ', x))
    df[coluna] = df[coluna].str.upper()
    return df[coluna]
    
def tratamento_coluna_numerica (df,coluna):
    df[coluna] = pd.to_numeric(df[coluna], errors='ignore')
    return df[coluna]

#df_recebidos['Valor'] = tratamento_coluna_numerica(df_recebidos, 'Valor')
df_recebidos['Valor'] = df_recebidos['Valor'].str.replace('+', '')    
df_recebidos['Valor'] = df_recebidos['Valor'].str.replace('-', '')   
df_recebidos['Valor'] = df_recebidos['Valor'].str.replace('.', '')   
df_recebidos['Valor'] = df_recebidos['Valor'].str.replace(',', '.')   
df_recebidos['Valor'] = df_recebidos['Valor'].str.replace(' ', '')   
df_recebidos['Valor'] = df_recebidos['Valor'].astype(float)   



situacao_recebidos = df_recebidos['Situação'].unique()
nome_arquivo = 'vendas'

df_recebidos.to_excel('../docs/exports/vendas.xlsx', index=False)






# for coluna in df_recebidos.columns:
#     print(coluna)
    
# type(plano['Vendas de produtos'])

# plano['Vendas de produtos']
# plano['Vendas no balcão']



#incluir colunas para cada loja



#filtrar coluna
#tabelas filtradas
#df_filtro =  