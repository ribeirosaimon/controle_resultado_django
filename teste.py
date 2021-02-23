import requests
import csv
import pandas as pd
import os

def convert_xlsx(nome_arquivo, nome_convertido):
    df = pd.read_excel(nome_arquivo)
    df.to_csv(nome_convertido+'.csv', index=False)
    os.remove(nome_arquivo)


url = 'http://b3.com.br/data/files/A0/F6/3B/CE/9B3B6710FB5A3B67AC094EA8/Cronograma%20de%20Eventos%20Corporativos%202021.xlsx'

def open_csv():
    lista_retorno = []
    with open('cronograma.csv', 'r') as arquivo_csv:
        empresas = csv.reader(arquivo_csv, delimiter=',')
        for x in empresas:
            dict_empresa = {
                x[0]:
                    {'primeiro_tri':x[12],
                    'segundo_tri':x[14],
                    'terceiro_tri':x[16]
                    }
                }
            lista_retorno.append(dict_empresa)
    return lista_retorno

print(open_csv())