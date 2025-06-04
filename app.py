import pandas as pd

# Carregar os dados do CSV
df = pd.read_csv('data/ceo_negros.csv')

# Mostrar os dados carregados
print(df)

# Exemplo: mostrar quantos CEOs negros tem por estado
print("\nContagem de CEOs negros por estado:")
print(df['Estado'].value_counts())
