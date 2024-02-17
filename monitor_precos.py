from utils.extracao import extrair_dados_produto
from utils.manipulacao import criar_dataframe, salvar_dataframe_excel


# URL para extrair os dados
url = "https://lista.mercadolivre.com.br/fone-de-ouvido_ITEM*CONDITION_2230284_NoIndex_True"

# Extrair os dados da página
resultado = extrair_dados_produto(url)

# Criar um DataFrame com os dados extraídos
df = criar_dataframe(resultado)

# Salvar o DataFrame em um arquivo Excel
nome_arquivo = 'tabela-produtos'
salvar_dataframe_excel(df, nome_arquivo)
