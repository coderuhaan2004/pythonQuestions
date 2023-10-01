def binary(a,l,r,x):        # a is the array, l is the left index, r is the right index, x is the element to be searched
    while l<=r:
        mid = l+(r-l)//2    # mid of the array
        if a[mid] == x:     # if element is present at the middle
            return mid
        elif a[mid] < x:    # if element is smaller than mid, then it can only be present in left subarray
            l = mid+1       # so we will search in left subarray
        else:               # else the element can only be present in right subarray
            r = mid-1       # so we will search in right subarray
    return -1               # if element is not present in array

#sorted array
l = [1,2,3,4,5,6,7,8,9,10]
x = 10#element to be searched
result = binary(l,0,len(l)-1,x) #function call
if result != -1:#if result is not -1
    print("Element is present at index",str(result))#print the index
else:#if result is -1
    print("Element is not present in array")#print the element is not present in array

    

