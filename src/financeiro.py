import pandas as pd
import os
import sys

from modules import mapBase as mb
import modules.mapBase as mb


listaArqruivos = mb.printLocalFiles('../docs/financeiro')
listaArqruivos = mb.allFiles('../docs/financeiro')

pd_financeiro = pd.read_excel(fr'../docs/financeiro/{listaArqruivos[0]}')
#pd_financeiro_santa_rosa = pd.read_excel(fr'docs/financeiro/{listaArqruivos[0]}')
#pd_financeiro_trevo = pd.read_excel(fr'docs/financeiro/{listaArqruivos[1]}')


#Trazer valores unicos de uma coluna
plano_de_contas = pd_financeiro['Plano de contas'].unique()
#Ordenar a coluna
plano_de_contas = sorted(plano_de_contas)
#Remover Duplicadas
plano_de_contas = plano_de_contas.drop_duplicates()


#incluir colunas para cada loja



#filtrar coluna
#tabelas filtradas
#df_filtro =  