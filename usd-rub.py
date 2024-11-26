import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import matplotlib.ticker as ticker


# Load the dataset
file_path = './data/USD_RUB Historical Data.csv'
data = pd.read_csv(file_path)

# Clean the data
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%y')
data.sort_values('Date', inplace=True)

# Line chart: Overall Trend
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Price'], label='Closing Price', color='blue', linewidth=2)
plt.title('USD/RUB Exchange Rate Trend', fontsize=16)
plt.ylabel('Price (RUB)', fontsize=14)
plt.legend(fontsize=12)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10)) 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=4)) 
plt.gca().yaxis.set_major_formatter('${x:,.0f}')
plt.grid(visible=True, which='major', axis='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()



# Histogram: Distribution of Daily Percentage Changes
data['Change %'] = data['Change %'].str.replace('%', '').astype(float)
plt.figure(figsize=(10, 6))
plt.hist(data['Change %'], bins=40, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution of Daily Percentage Changes in USD/RUB Exchange Rate', fontsize=16)
plt.xlabel('Percentage Change (%)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
x_ticks = np.linspace(data['Change %'].min(), data['Change %'].max(), 15) 
plt.xticks(x_ticks, labels=[f'{tick:.1f}%' for tick in x_ticks], fontsize=10)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()



# Rolling Average: Smoothing the Trends
data['7-Day MA'] = data['Price'].rolling(window=7).mean()
data['30-Day MA'] = data['Price'].rolling(window=30).mean()
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Price'], label='Daily Closing Price', alpha=0.6)
plt.plot(data['Date'], data['7-Day MA'], label='7-Day Moving Average', color='red', linewidth=1.5)
plt.plot(data['Date'], data['30-Day MA'], label='30-Day Moving Average', color='green', linewidth=1.5)
plt.title('USD/RUB Exchange Rate Trends', fontsize=16)
plt.ylabel('Price (RUB)', fontsize=12)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=4)) 
plt.legend()
plt.grid(True)
plt.show()





