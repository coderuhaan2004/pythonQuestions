import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = ''
data = pd.read_csv(file_path)

height = data['Height'].values
weight = data['Weight'].values

correlation = np.corrcoef(height,weights)[0,1]

plt.figure(figsize = (10,6))
plt.scatter(height,weight,s=10,alpha = 0.5)
plt.title()
plt.xlabel()
plt.ylabel()

fit = np.polyfit(heights,weights,1)#
fit_fn = np.polyfit(fit)#
plt.plot(heights,fit_fn(heights))#

plt.show()

'''*height = data['Height'].values extracts the 'Height' column from the DataFrame data and converts it into a NumPy array. This allows you to use NumPy functions and operations on the 'height' data.

*correlation = np.corrcoef(h,w)[0,1]
Correlation is actually a 2x2 matrix:
    [correlation(h,h)   correlation(h,w)]
    [correlation(w,h)   correlation(w,w)]
as we want to access 0th row and 1st column, we have used [0,1] indexing.
correlation coeffcient has values -1,0,1 only

*plt.figure(figsize=(width,height)) creates a canvas of width w and height h

*plt.scatter(x-axis,y-axis,sizeofmarker(in pixels),alpha(transparency))

*fit = np.polyfit(heights,weights,degree of polynomial) Creates an array of slopes m and y intercept b 

fit_fn = np.polyfit1d(fit)
plt.plot(heights(heights, fit_fn(heights) means the values of weights with corresponding heights in straight line








