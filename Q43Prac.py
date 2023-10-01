import pandas as pd

file_path = ''
data = pd.read_csv(file_path)
dates = pd.to_datetime(data['name of Column'])
prices = data['Name of the column'] #list of data

local_minima_indices = []
local_maxima_indices = []

for i in range(1,len(prices)-1):
    if prices[i-1]>prices[i]<prices[i+1]:
        local_minima_indices.append(i)
#same for local maxima

local_minima_dates = dates.iloc[local_minima_indices]
local_maxima_dates = dates.iloc[local_maxima_indices]

print(local_minima_dates)


'''Integer location - iloc
dates.iloc[local_minima_indices] means that retrieve the data from the dates column according to the indices present in the list (local_maxi/minima_indices)

for example:
    local_minima_dates = dates.iloc[3,7,10] means that retrrieve the data from dates column of only the positions 3,7 and 10```
