import numpy as np #import module numpy
import pandas as pd #import module pandas
import matplotlib.pyplot as plt #import module matplotlib.pyplot

# Load the CSV file into a DataFrame
csv_file = '/home/ruhaan/Desktop/New Folder/Q44 - HeightWeight.csv'#path of the csv file
data = pd.read_csv(csv_file) #read the csv file

# Extract height and weight data from the DataFrame
heights = data['Height'].values #extract height data from the DataFrame
weights = data['Weight'].values #extract weight data from the DataFrame

# Calculate the correlation coefficient
correlation = np.corrcoef(heights, weights)[0, 1] #calculate the correlation coefficient

# Create a scatter plot and fit a line that is closest to the data points
plt.figure(figsize=(10, 6)) #set the figure size
plt.scatter(heights, weights, s=10, alpha=0.5) #scatter plot
plt.title("Height vs Weight Scatter Plot") #set the title of the plot
plt.xlabel("Height")#set the x label of the plot
plt.ylabel("Weight")#set the y label of the plot

# Fit a linear regression line
fit = np.polyfit(heights, weights, 1)#fit a linear regression line
fit_fn = np.poly1d(fit)#fit a linear regression line
plt.plot(heights, fit_fn(heights), color='red', linewidth=2)#plot the linear regression line

plt.show()#show the plot

# Display the correlation coefficient
print(f"Correlation coefficient: {correlation}")#print the correlation coefficient

