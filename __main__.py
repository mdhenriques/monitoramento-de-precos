from utils.extracao import  extrair_dados_varias_paginas
from utils.manipulacao import criar_dataframe, salvar_dataframe_excel

def main():
    base_url = "https://lista.mercadolivre.com.br/fone-de-ouvido_ITEM*CONDITION_2230284_NoIndex_True"

    num_paginas = 3

    dados_totais = extrair_dados_varias_paginas(base_url, num_paginas)

    df = criar_dataframe(dados_totais)

    nome_arquivo = 'tabela-produtos'
    salvar_dataframe_excel(df, nome_arquivo)

if __name__ == "__main__":
    main()