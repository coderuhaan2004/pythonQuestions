#a program to find median of a list of numbers but without sorting it.

def median(lst): # function to find median
    left = []    # creating empty lists
    right = []   # creating empty lists
    pivot = lst[0] # taking first element as pivot
    for i in range(1, len(lst)): # looping through the list
        if lst[i] < pivot:  # if element is less than pivot
            left.append(lst[i]) # append it to left list
        elif lst[i] > pivot: # if element is greater than pivot
            right.append(lst[i]) # append it to right list
        else: # if element is equal to pivot
            pass # do nothing
    if len(left) == len(right): # if length of left list is equal to right list
        return pivot # return pivot
    elif len(left) > len(right): # if length of left list is greater than right list
        return median(left) # return median of left list
    else: # if length of left list is less than right list
        return median(right) # return median of right list
# taking list of 10 random numbers
arr = [22,15,16,22,65,18,23,27,48,36]   #random list
print("The given array is: ", arr)      #returning the list
print("The median is: ", median(arr))   #returning the median of the list


