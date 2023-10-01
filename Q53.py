import random       #importing module to create random array of numbers
def quickso(a):     # defining a function to sort the array
    if len(a)<=1:   # if the array has only one element or no element then return the array
        return a    # base case
    else:           # if the array has more than one element then sort the array
        pivot = a[0]# take the first element as pivot
        left = []   # create two empty arrays
        right = []  # one for elements less than pivot and other for elements greater than pivot
        for i in range(1,len(a)): # loop to sort the array
            if a[i]<pivot:      # if element is less than pivot then append it to left array
                left.append(a[i])#appending element to left array
            else:               # if element is greater than pivot then append it to right array
                right.append(a[i])#appending element to right array
        return quickso(left)+[pivot]+quickso(right) # example of recursion
# take a array of 10 random numbers
a = [random.randint(1,100) for i in range(10)]      # creating a random array of 10 numbers
print("The unsorted array was: ",a)                 # printing the unsorted array
print("The Sorted array is: ",quickso(a))           # printing the sorted array


