# Análise exploratória de Dados (AED)

import pandas as pd


df = pd.read_csv('clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y',errors='coerce')

print(f"Verificação inicial:")
print(df.info())

print(f"Análise dos dados nulos: \n {df.isnull().sum()}")
print(f"% de dados nulos: \n {df.isnull().mean() * 100}") # .mean() = média
print(f"Totais de dados nulos: \n {df.isnull().mean().sum() * 100}")

df.dropna(inplace=True)

print(f"Confirmar remoção de dados nulos: \n {df.isnull().sum().sum()}")

print(f"Análise de daods duplicados: \n {df.duplicated().sum()}")

print(f"Análise de dados únicos: \n {df.nunique()}") # Busca a quantidade de valores únicos

print(f"Estatísticas dos dados: \n {df.describe()}") # std -> desvio padrão

# Criar um novo dataFrame para não ser possível identificar o usuário por questões de LGPD
df = df[['idade', 'data', 'estado', 'salario', 'nivel_educacao', 'numero_filhos', 'estado_civil', 'area_atuacao']]
print(f"Novo DataFrame: \n {df.head().to_string()}")

df.to_csv('clientes-v2-tratados.csv', index=False)