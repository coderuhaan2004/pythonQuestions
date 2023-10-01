import pandas as pd #importing pandas library

# Load the CSV data into a pandas DataFrame
file_path = '/home/ruhaan/Desktop/New Folder/Stocks.csv'#path of the csv file
data = pd.read_csv(file_path)#reading the csv file
dates = pd.to_datetime(data['Date'])  # Assuming 'Date' contains the dates
prices = data['Close']  # Assuming 'Close' contains the prices

# Initialize lists to store indices of local minima and maxima
local_minima_indices = [] #empty list of local minima
local_maxima_indices = [] #empty list of local maxima

# Loop through the dataset to find points of local minima and maxima
for i in range(1, len(prices) - 1):#looping through the prices
    if prices[i - 1] > prices[i] < prices[i + 1]:#if price is less than the previous and next price, it is a local minima
        local_minima_indices.append(i)#appending the index of local minima
    elif prices[i - 1] < prices[i] > prices[i + 1]:#if price is greater than the previous and next price, it is a local maxima
        local_maxima_indices.append(i)#appending the index of local maxima

# Get the corresponding dates for local minima and maxima
local_minima_dates = dates.iloc[local_minima_indices]#getting the dates of local minima
local_maxima_dates = dates.iloc[local_maxima_indices]#getting the dates of local maxima

#Write a code to Buy stocks on local minima and sell on local maximas to maximize profit

#assuming we sell only one stock at each local maxima
principal = 100000#initial principal
stocks = 0#initial stocks
for i in range(len(local_minima_indices)):#looping through the local minima
    stocks+=1#buying one stock at each local minima
    principal -= prices[local_minima_indices[i]]#subtracting the price of the stock from the principal
while stocks > 0:#looping through the local maxima
    for i in range(len(local_maxima_indices)):#looping through the local maxima
        principal += prices[local_maxima_indices[i]]#adding the price of the stock to the principal
        stocks -= 1#selling the stock
print("Case 1: Sold only one stock at local max: ",principal)#printing the principal

#assuming I buy all stocks at their local minima and sell all stocks at global maxima
principal = 100000#initial principal
stocks = 0#initial stocks
for i in range(len(local_minima_indices)):#looping through the local minima
    stocks+=1#buying one stock at each local minima
    principal -= prices[local_minima_indices[i]]#subtracting the price of the stock from the principal
principal += max(prices[local_maxima_indices])*stocks #global maxima
print("Case 2: Sold all stocks at global max: ",principal)#printing the principal

#assuming I buy all stocks at their local minima and sell on days when the price is greater than some price such that my profit is maximized
principal = 100000#initial principal
stocks = 0#initial stocks
principi = 0#initial profit
for i in range(len(local_minima_indices)):#looping through the local minima
    stocks+=1#buying one stock at each local minima
    principal -= prices[local_minima_indices[i]]#subtracting the price of the stock from the principal
possible_principals = []#empty list of possible principals
for j in range(12000,16000):#looping through the prices
    while stocks > 0:#looping through the stocks
        for i in range(len(prices)):#looping through the prices
            if prices[len(prices)-i-1] > j: #as in the latest dates, the prices are very large and hence profit is very large
                principi += principal + prices[i]#adding the price of the stock to the principal
                stocks -= 1#selling the stock
    possible_principals.append(principi)#appending the possible principals
principal = max(possible_principals)#maximizing the principal
print("Case 3: Sold one stock at price greater than some prices with corresponding max profit: ",principal)#printing the principal






