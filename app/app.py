import pandas as pd
excel = pd.read_excel("app\dadoss.xlsx")

mes = input("Qual o mes ?")

analise = excel.sort_values(by=f'{mes}', ascending=False)

print(analise)
