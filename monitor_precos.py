import requests
from bs4 import BeautifulSoup

def extrair_dados_produto(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    produtos = []
    for item in soup.find_all('li', class_='ui-search-layout__item'):
        
        nome_produto = item.find('h2', class_='ui-search-item__title').text.strip()
        
        preco_produto = item.find('span', class_='andes-money-amount__fraction').text.strip()
        produtos.append({'nome':nome_produto, 'preco': preco_produto})
    return produtos
resultado = extrair_dados_produto("https://lista.mercadolivre.com.br/fone-de-ouvido_ITEM*CONDITION_2230284_NoIndex_True")

print(len(resultado))