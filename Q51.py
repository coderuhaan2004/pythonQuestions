def bubble(a):      #this is the bubble sort algorithm  
    for i in range(len(a)): #this makes sure that the last element is sorted and is not checked again
        for j in range(len(a)-i-1): #this is the loop that checks the elements
            if(a[j]>a[j+1]):#if the next element is smaller than the current element then swap them
                a[j],a[j+1] = a[j+1],a[j] #swapping
    return a    #returning the sorted array
arr = [5,6,3,8,1,0] #the array to be sorted
print("Unsorted array",arr)  #printing the unsorted array
print("Sorted array",bubble(arr))  #printing the sorted array
