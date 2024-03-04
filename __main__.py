from utils.extracao import  extrair_dados_varias_paginas, extrair_dados_produto
from utils.manipulacao import criar_dataframe

def main():
    base_url = "https://lista.mercadolivre.com.br/fone-de-ouvido_ITEM*CONDITION_2230284_NoIndex_True"

#    num_paginas = 3

#    dados_totais = extrair_dados_varias_paginas(base_url, num_paginas)


    dados_totais = extrair_dados_produto(base_url)

    filtro = "Fone De Ouvido"
    df = criar_dataframe(dados_totais, filtro)
    
    df.to_json('tabela-produtos', orient='records', indent=4)

if __name__ == "__main__":
    main()