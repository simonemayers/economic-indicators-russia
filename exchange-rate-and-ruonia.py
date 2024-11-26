import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import seaborn as sns



# Load the datasets
exchange_rate_data = pd.read_csv('./data/USD_RUB Historical Data.csv', sep=',')
ruonia_data = pd.read_csv("./data/Ruonia01_01_2022_T02_10_2024.csv", sep=',')
ruonia_data = ruonia_data.rename(columns={'ruo': 'Rate', 'DT': 'Date'})  
ruonia_data['vol'] = pd.to_numeric(ruonia_data['vol'], errors='coerce')
ruonia_data['Date'] = pd.to_datetime(ruonia_data['Date'])
exchange_rate_data = exchange_rate_data.rename(columns={'Price': 'ExchangeRate'})
exchange_rate_data['Date'] = pd.to_datetime(exchange_rate_data['Date'])
merged_data = pd.merge(ruonia_data, exchange_rate_data, on='Date', how='inner')



# Time Series Overlay: RUONIA Rate vs USD/RUB Exchange Rate
plt.figure(figsize=(14, 7))
plt.plot(merged_data['Date'],merged_data['Rate'],label='RUONIA Rate',color='blue',linewidth=1.5)
plt.plot(merged_data['Date'], merged_data['ExchangeRate'], label='USD/RUB Exchange Rate', color='orange', linewidth=1.5)
plt.ylabel('RUONIA Rate & USD/RUB Exchange Rate', fontsize=12, color='black')
plt.title('RUONIA Rate vs USD/RUB Exchange Rate Over Time', fontsize=14)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()


# Scatter Plot: RUONIA Rate vs USD/RUB Exchange Rate
plt.figure(figsize=(10, 7))
scatter = plt.scatter(
    merged_data['Rate'], 
    merged_data['ExchangeRate'], 
    c=merged_data['Date'].apply(lambda x: x.toordinal()), 
    cmap='viridis', s=50, alpha=0.8, edgecolors='k'
)
plt.xlabel('RUONIA Rate (%)', fontsize=12)
plt.ylabel('USD/RUB Exchange Rate', fontsize=12)
plt.title('RUONIA Rate vs USD/RUB Exchange Rate', fontsize=14, fontweight='bold')
plt.grid( color='lightgray', linestyle='--', linewidth=0.5, alpha=0.7)
cbar = plt.colorbar(scatter)
cbar.set_label('Date (Gradient)', fontsize=10)
plt.tight_layout()
plt.show()



# Heatmap of Correlations
column_mapping = {
    'Rate': 'RUONIA Rate','vol': 'Trading Volume','T': 'Transaction Count','C': 'Clearing Count','ExchangeRate': 'USD/RUB Exchange Rate'
}
numeric_data = merged_data.select_dtypes(include=['float64', 'int64'])
numeric_data = numeric_data.rename(columns=column_mapping)
correlations = numeric_data.drop(columns=['StatusXML', 'High', 'Low', 'MinRate', 'MaxRate', 'Open', 'Percentile25', 'Percentile75']).corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f", center=0, vmin=-1, vmax=1, linewidths=0.5, linecolor='white')
plt.title('Correlation Heatmap: RUONIA and USD/RUB Exchange Rate', fontsize=16, pad=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10) 
plt.tight_layout()
plt.show()



# USD/RUB Exchange Rate Volatility and RUONIA Rate
exchange_rate_data['Returns'] = exchange_rate_data['ExchangeRate'].pct_change()
exchange_rate_data['Change %'] = exchange_rate_data['Change %'].str.replace('%', '').astype(float)
exchange_rate_data['Volatility'] = exchange_rate_data['Change %'].rolling(window=30).std()
plt.figure(figsize=(14, 7))
plt.plot(exchange_rate_data['Date'], exchange_rate_data['Volatility'], label='USD/RUB Exchange Rate Volatility', color='orange', linewidth=1.5)
plt.plot(ruonia_data['Date'], ruonia_data['Rate'], label='RUONIA Rate', color='blue', linewidth=1.5)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(2))
plt.ylabel('Volatility / Rate', fontsize=12, labelpad=10)
plt.title('USD/RUB Exchange Rate Volatility vs RUONIA Rate', fontsize=16, pad=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.grid(axis='y', alpha=0.6, linestyle=':')
plt.tight_layout
plt.show()




