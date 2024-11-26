import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import matplotlib.ticker as ticker



# Load the dataset 
ruonia_data = pd.read_csv("./data/Ruonia01_01_2022_T02_10_2024.csv", sep=',')
ruonia_data['DT'] = pd.to_datetime(ruonia_data['DT'])  # Convert date to datetime format
ruonia_data = ruonia_data.rename(columns={'DT': 'Date', 'ruo': 'Rate'})  # Rename columns
ruonia_data['vol'] = pd.to_numeric(ruonia_data['vol'], errors='coerce')


# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(ruonia_data['Date'], ruonia_data['Rate'], label='RUONIA Rate', color='blue', linewidth=2, alpha=0.7)
plt.ylabel('Rate', fontsize=14)
plt.title('Russian Overnight Index Average (RUONIA) Rate Over Time')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.grid()
plt.show()


#RUONIA Rate Distribution
plt.figure(figsize=(12, 8))
ruonia_data['Rate'].plot(kind='hist', bins=30, color='blue', alpha=0.7)
plt.title('Distribution of RUONIA Rates', fontsize=16)
plt.xlabel('Rate', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.grid( axis='y', alpha=0.3)
plt.show()


#Rate over Time with Confidence Intervals
plt.figure(figsize=(12, 6))
plt.plot(ruonia_data['Date'], ruonia_data['Rate'], label='RUONIA Rate', color='blue')
plt.fill_between(ruonia_data['Date'], ruonia_data['MinRate'], ruonia_data['MaxRate'], color='blue', alpha=0.2, label='Min-Max Range')
plt.ylabel('Rate', fontsize=14)
plt.title('RUONIA Rate Over Time with Min/Max Range', fontsize=16)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) 
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(2))
plt.legend()
plt.grid( axis='y', alpha=0.3)
plt.show()


#Volume Traded Over Time
plt.figure(figsize=(12, 6))
plt.plot(ruonia_data['Date'], ruonia_data['vol'], label='Trading Volume', color='orange')
plt.ylabel('Volume', fontsize=14)
plt.title('RUONIA Trading Volume Over Time', fontsize=16)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(100))
plt.grid( axis='y', alpha=0.3)
plt.show()


#Correlation Matrix 
correlation_matrix = ruonia_data[['Rate', 'vol', 'MinRate', 'MaxRate']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt=".2f", linewidths=0)
plt.title("Correlation Matrix of RUONIA Metrics", fontsize=16, pad=20)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()


#Percentile Trends Over Time
plt.figure(figsize=(12, 6))
plt.plot(ruonia_data['Date'], ruonia_data['Percentile25'], label='25th Percentile', color='blue', linestyle='solid', linewidth=2)
plt.plot(ruonia_data['Date'], ruonia_data['Percentile75'], label='75th Percentile', color='orange', linestyle='solid', linewidth=2)
plt.ylabel('RUONIA RATE (%)')
plt.title('Percentile Trends of RUONIA Rate')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) 
plt.legend(loc='upper right', frameon=True, fontsize=10, shadow=True)
plt.grid(color='gray', linestyle='--', linewidth=0.5, axis='y', alpha=0.3)
plt.show()



#Rolling Average of RUONIA Rate
ruonia_data['7-Day'] = ruonia_data['Rate'].rolling(window=7).mean()
ruonia_data['30-Day'] = ruonia_data['Rate'].rolling(window=30).mean()
plt.figure(figsize=(12, 6))
plt.plot(ruonia_data['Date'], ruonia_data['Rate'], label='Daily RUONIA Rate', color='blue', alpha=0.5)
plt.plot(ruonia_data['Date'], ruonia_data['7-Day'], label='7-Day Rolling Avg', color='red', linewidth=1.5)
plt.plot(ruonia_data['Date'], ruonia_data['30-Day'], label='30-Day Rolling Avg', color='green', linewidth=1.5)
plt.ylabel('Rate', fontsize=14)
plt.title('RUONIA Rate with 7-Day Rolling Average', fontsize=16)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=4)) 
plt.legend()
plt.grid()
plt.show()


