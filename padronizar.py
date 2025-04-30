import pandas as pd
import numpy as np


df = pd.read_excel("Base_despadronizada.xlsx", dtype=str)

df['sexo'] = df['sexo'].str.lower().str.strip()
df['sexo'] = df['sexo'].replace({
    'm': 'Masculino', 'masc': 'Masculino', 'masculino': 'Masculino',
    'f': 'Feminino', 'fem': 'Feminino', 'feminino': 'Feminino'
})


def clean_grade(series):

    extracted = series.str.extract(r'(\d+)[,.]?(\d*)')
    
    def combine(row):
        if pd.isna(row[1]) or row[1] == '':
            return row[0]
        return f"{row[0]}.{row[1]}"
    
    combined = extracted.apply(combine, axis=1)
    
    num = pd.to_numeric(combined, errors='coerce')
    
    num = num.where((num >= 0) & (num <= 10), np.nan)
    return num

df['nota_matematica'] = clean_grade(df['nota_matematica'])


df['nota_portugues'] = clean_grade(df['nota_portugues'])

df['frequencia'] = pd.to_numeric(df['frequencia'].str.extract(r'(\d+)')[0], errors='coerce')
df['frequencia'] = df['frequencia'].where((df['frequencia'] >= 0) & (df['frequencia'] <= 100), np.nan)

df['media'] = (df['nota_matematica'].fillna(0) + 
              df['nota_portugues'].fillna(0) + 
              (df['frequencia'].fillna(0) / 10)) / 3

df['aprovado'] = np.where(df['media'] >= 7, 'Sim', 'Não')

df.to_excel("Base_tratada.xlsx", index=False)

print("✅ Arquivo 'Base_tratada.xlsx' criado com sucesso!")