import pandas as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Criar um datafram apenas com as colunas idade e salário para análise
df = df[['idade', 'salario']]

# Normalização dos dados - MinMaxScaler valores padrões
scaler = MinMaxScaler() # intervalo padrão é de [0, 1]
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])
print(f"Valores padrões do MinMaxScaler: \n {df.head()} ")

# Normalização dos dados - MinMaxScaler valores ajustados
min_max_scaler = MinMaxScaler(feature_range=(-1, 1)) # intervalo customizado de [-1, 1]
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])
print(f"Valores ajustados do MinMaxScaler: \n {df.head()} ")

# Padronização - StandardScaler
scaler = StandardScaler() # média será 0 (zero) e o desvio padrão será 1
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']])
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])
print(f"Valores padrões do StandardScaler: \n {df.head()} ")

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']])
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])
print(f"Valores padrões do RobustScaler: \n {df.head()} ")

print("MinMaxScaler (de 0 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(
    df['idadeMinMaxScaler'].min(),
    df['idadeMinMaxScaler'].max(),
    df['idadeMinMaxScaler'].mean(),
    df['idadeMinMaxScaler'].std()
))

print("Salário - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(
    df['salarioMinMaxScaler'].min(),
    df['salarioMinMaxScaler'].max(),
    df['salarioMinMaxScaler'].mean(),
    df['salarioMinMaxScaler'].std()
))

print("\n MinMaxScaler (de -1 a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(
    df['idadeMinMaxScaler_mm'].min(),
    df['idadeMinMaxScaler_mm'].max(),
    df['idadeMinMaxScaler_mm'].mean(),
    df['idadeMinMaxScaler_mm'].std(),
))

print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(
    df['salarioMinMaxScaler_mm'].min(),
    df['salarioMinMaxScaler_mm'].max(),
    df['salarioMinMaxScaler_mm'].mean(),
    df['salarioMinMaxScaler_mm'].std(),
))

print("\n StandardScaler (Ajuste a médio a 0 e devio padrão a 1):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(
    df['idadeStandardScaler'].min(),
    df['idadeStandardScaler'].max(),
    df['idadeStandardScaler'].mean(),
    df['idadeStandardScaler'].std(),
))

print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.18f} Std: {:.4f}".format(
    df['salarioStandardScaler'].min(),
    df['salarioStandardScaler'].max(),
    df['salarioStandardScaler'].mean(),
    df['salarioStandardScaler'].std(),
))

print("\n RobustScaler (Ajuste a mediana e IQR):")
print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(
    df['idadeRobustScaler'].min(),
    df['idadeRobustScaler'].max(),
    df['idadeRobustScaler'].mean(),
    df['idadeRobustScaler'].std(),
))

print("Idade - Min: {:.4f} Max: {:.4f} Mean: {:.4f} Std: {:.4f}".format(
    df['salarioRobustScaler'].min(),
    df['salarioRobustScaler'].max(),
    df['salarioRobustScaler'].mean(),
    df['salarioRobustScaler'].std(),
))