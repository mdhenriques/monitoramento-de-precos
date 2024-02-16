import requests
from bs4 import BeautifulSoup
import pandas as pd

def criar_dataframe(resultado):
    df = pd.DataFrame(resultado)
    return df

def salvar_dataframe_excel(df, nome_arquivo):
    df.to_excel(nome_arquivo + '.xlsx', index=False, engine='xlsxwriter')
    print(f'DataFrame salvo como {nome_arquivo}')

def extrair_dados_produto(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    produtos = []
    for item in soup.find_all('li', class_='ui-search-layout__item'):
        
        nome_produto = item.find('h2', class_='ui-search-item__title').text.strip()
        
        preco_produto = item.find('span', class_='andes-money-amount__fraction').text.strip()

        centavos_existe = item.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-24')
        centavos = centavos_existe.text.strip() if centavos_existe else '00'

        produtos.append({'nome':nome_produto, 'preco': preco_produto + ',' + centavos})

    return produtos


resultado = extrair_dados_produto("https://lista.mercadolivre.com.br/fone-de-ouvido_ITEM*CONDITION_2230284_NoIndex_True")

df = criar_dataframe(resultado)

salvar_dataframe_excel(df, 'tabela-produtos')


