import pandas as pd

def criar_dataframe(resultado):
    df = pd.DataFrame(resultado)
    return df

def salvar_dataframe_excel(df, nome_arquivo):
    df.to_excel(nome_arquivo + '.xlsx', index=False, engine='xlsxwriter')
    print(f'DataFrame salvo como {nome_arquivo}.xlsx')
