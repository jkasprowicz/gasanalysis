import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo
df = pd.read_excel('/Users/joaokasprowicz/Desktop/base.xlsx')
# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo

# Certifique-se de que a coluna de datas está no formato correto
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
df.set_index('Date', inplace=True)


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['CH4'], marker='o', linestyle='-')
plt.title('CH4 Durante o Tempo')
plt.xlabel('Data')
plt.ylabel('CH4')
plt.grid(True)
plt.show()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['N2O'], marker='o', linestyle='-')
plt.title('N20 Durante o Tempo')
plt.xlabel('Data')
plt.ylabel('N20')
plt.grid(True)
plt.show()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['CO2'], marker='o', linestyle='-')
plt.title('CO2 Durante o Tempo')
plt.xlabel('Data')
plt.ylabel('CO2')
plt.grid(True)
plt.show()

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Temp'], marker='o', linestyle='-')
plt.title('Temperatura Durante o Tempo')
plt.xlabel('Data')
plt.ylabel('Temperatura')
plt.grid(True)
plt.show()



# Função para decomposição e plotagem
def decompose_and_plot(series, variable_name):
    result = seasonal_decompose(series, model='additive', period=12)  # ajuste o período conforme necessário

    plt.figure(figsize=(12, 8))

    plt.subplot(4, 1, 1)
    plt.plot(series, label='Original')
    plt.legend(loc='upper left')
    plt.title(f'{variable_name} - Série Temporal Original')

    plt.subplot(4, 1, 2)
    plt.plot(result.trend, label='Tendência')
    plt.legend(loc='upper left')
    plt.title(f'{variable_name} - Tendência')

    plt.subplot(4, 1, 3)
    plt.plot(result.seasonal, label='Sazonalidade')
    plt.legend(loc='upper left')
    plt.title(f'{variable_name} - Sazonalidade')

    plt.subplot(4, 1, 4)
    plt.plot(result.resid, label='Resíduos')
    plt.legend(loc='upper left')
    plt.title(f'{variable_name} - Resíduos')

    plt.tight_layout()
    plt.show()

# Aplicar a decomposição e plotagem para cada variável
decompose_and_plot(df['Temp'], 'Temperatura')
decompose_and_plot(df['CO2'], 'CO2')
decompose_and_plot(df['CH4'], 'CH4')
decompose_and_plot(df['N2O'], 'N2O')
