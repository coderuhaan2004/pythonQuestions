import pandas as pd

# Load the CSV data into a pandas DataFrame
file_path = '/home/ruhaan/Desktop/New Folder/Stocks.csv'
data = pd.read_csv(file_path)
dates = pd.to_datetime(data['Date'])  # Assuming 'Date' contains the dates
prices = data['Close']  # Assuming 'Close' contains the prices

# Initialize lists to store indices of local minima and maxima
local_minima_indices = []
local_maxima_indices = []

# Loop through the dataset to find points of local minima and maxima
for i in range(1, len(prices) - 1):
    if prices[i - 1] > prices[i] < prices[i + 1]:
        local_minima_indices.append(i)
    elif prices[i - 1] < prices[i] > prices[i + 1]:
        local_maxima_indices.append(i)

# Get the corresponding dates for local minima and maxima
local_minima_dates = dates.iloc[local_minima_indices]
local_maxima_dates = dates.iloc[local_maxima_indices]

# Buy at every local minima and sell at every local maxima
principal = 100000
stocks = 0
j = 0  # Index for local_maxima_indices

for i in range(len(prices)):
    if j < len(local_maxima_indices) and i == local_maxima_indices[j] and stocks > 0:
        # Sell one stock at local maxima
        principal += prices[i]
        stocks -= 1
        j += 1
    elif i in local_minima_indices and principal > prices[i]:
        # Buy one stock at local minima
        stocks += 1
        principal -= prices[i]

print("Final balance: ", principal)

