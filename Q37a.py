import random #Using random module to generate random numbers

a = [] #Creating an empty list
for i in range(0, 100): #looping through 100 times
    a.append([]) #appending empty list to the list a

empty = 100 #initializing empty bins to 100
balls_added = 0 #initializing balls added to 0

while empty > 0: #looping until empty bins are 0
    bin_index = random.randint(0, 99) #generating random number between 0 and 99
    a[bin_index].append(0) #appending 0 to the bin_index
    balls_added += 1 #incrementing balls added by 1

    if len(a[bin_index]) == 1: #checking if the bin is empty
        empty -= 1 #decrementing empty bins by 1

print("Total number of balls added:", balls_added) #printing total number of balls added
print("Total number of empty bins:", empty) #printing total number of empty bins
empty = 100  # Reset empty bins to 100 for the next run.

