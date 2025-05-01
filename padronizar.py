import pandas as pd

df = pd.read_csv('Base_despadronizada.csv')

sexo_map = {
    'm': 'Masculino', 'masc': 'Masculino', 'masculino': 'Masculino', 'MASC': 'Masculino', 'M': 'Masculino',
    'f': 'Feminino', 'fem': 'Feminino', 'feminino': 'Feminino', 'FEM': 'Feminino', 'F': 'Feminino'
}
df['sexo'] = df['sexo'].str.strip().str.lower().map(sexo_map)

df['nota_matematica'] = df['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
df['nota_portugues'] = df['nota_portugues'].astype(str).str.replace(',', '.').astype(float)

df['media'] = (df['nota_matematica'] + df['nota_portugues'] + (df['frequencia'] / 10)) / 3
df['media'] = df['media'].round(2)

df['aprovado'] = df['media'].apply(lambda x: 'Sim' if x >= 7 else 'Não')

# Gerar como arquivo Excel
df.to_excel('Base_tratada.xlsx', index=False)
