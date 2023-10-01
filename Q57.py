def max_subarray(a):# define a function that takes in an array
    max_sum = -float('inf') # initialize max_sum to negative infinity
    current_sum = 0# initialize current_sum to 0
    start = end = s = 0# initialize start, end, and s to 0
    for i,x in enumerate(a):# loop through the array
        if current_sum <= 0: # if current_sum is negative, then we can start a new subarray
            s = i # start a new subarray
            current_sum = x # reset current_sum
        else: # if current_sum is positive, then we can continue the subarray
            current_sum += x # continue the subarray
        if current_sum > max_sum: # if current_sum is greater than max_sum, then we have a new max_sum
            start = s # update start
            end = i # update end
            max_sum = current_sum # update max_sum
    return a[start:end+1], max_sum # return the subarray and the max_sum

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]# define an array
print(max_subarray(a)) # ([4, -1, 2, 1], 6)# print the result of the function
