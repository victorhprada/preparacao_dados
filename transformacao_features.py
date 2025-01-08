import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Transformação Logaritmica
df['salario_log'] = np.log1p(df['salario']) # log1- é usado para evirar problemas com valores zero
print(f"\nDataFrame após transformação logaritmica no salário: \n {df.head()}")

# Transformação Box-Cox
df['salario_boxcox'], _ = stats.boxcox(df['salario'] + 1)
print(f"DataFrame após transformação Box-Cox no salário: \n {df.head()}")

# Codoficação de frequência para estados
estado_freq = df['estado'].value_counts() / len(df)
df['estado_freq'] = df['estado'].map(estado_freq)
print(f"DataFrame após codificação de frequência para os estados: \n {df.head()}")

# Codoficação de frequência para idade
idade_freq = df['idade'].value_counts() / len(df)
df['idade_freq'] = df['idade'].map(idade_freq)
print(f"DataFrame após codificação de frequência para os nomes: \n {df.head()}")

# Interações
df['interacao_dade_filhos'] = df['idade'] * df['numero_filhos']
print(f"DataFrame após interações: \n {df.head()}")