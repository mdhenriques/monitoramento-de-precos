import pandas as pd

def criar_dataframe(resultado, filtro):
    dfBruto = pd.DataFrame(resultado)
    
    dfFiltrado = dfBruto[dfBruto['nome'].str.contains(filtro, case=False)]
    
    return dfFiltrado

