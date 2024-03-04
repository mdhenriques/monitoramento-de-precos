import requests
from bs4 import BeautifulSoup
from produto import Produto
import re

def extrair_MLB(url):
    padrao1 = r"MLB-(\d+)"
    padrao2 = r"p/MLB(\d+)"
    response = requests.get(url)
    
    if response.status_code == 200:
        URL = response.url
        match = re.search(padrao1, URL)

        if match:
            return match.group(1)
        
        match = re.search(padrao2, URL)
        if match:
            return match.group(1)
    
    
    
    

def extrair_dados_produto(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    produtos = []
    for item in soup.find_all('li', class_='ui-search-layout__item'):
        link_tag = item.find('a', class_='ui-search-item__group__element ui-search-link__title-card ui-search-link')
        link = link_tag.get('href')
        MLB = extrair_MLB(link)        

        nome_produto = item.find('h2', class_='ui-search-item__title').text.strip()

        
        preco_produto = item.find('span', class_='andes-money-amount__fraction').text.strip()
        centavos_existe = item.find('span', class_='andes-money-amount__cents andes-money-amount__cents--superscript-24')
        centavos = centavos_existe.text.strip() if centavos_existe else '00'

        numero_de_avaliacoes_existe = item.find('span', class_='ui-search-reviews__amount')
        numero_de_avaliacoes = numero_de_avaliacoes_existe.text.strip().replace("(", "").replace(")", "") if numero_de_avaliacoes_existe else '0'

        avaliacao_media = item.find('span', class_='ui-search-reviews__rating-number').text.strip() if numero_de_avaliacoes_existe else 'null'        

        produto = Produto(MLB, nome_produto, preco_produto, avaliacao_media, numero_de_avaliacoes)
        
        produtos.append({'MLB': produto.MLB, 'nome': produto.nome, 'preco': produto.preco + ',' + centavos, 'avaliacao media': produto.avaliacao_media, 'numero de avaliacoes': produto.num_avaliacoes})
    
    return produtos

def extrair_dados_varias_paginas(base_url, num_paginas):
    dados_totais = []
    for pagina in range(1, num_paginas + 1):
        if pagina == 1:
            url = base_url
        else:
            url = f"{base_url}_Desde_{(pagina - 1) * 50 + 1}"
        dados_pagina = extrair_dados_produto(url)
        dados_totais.extend(dados_pagina)
    return dados_totais

