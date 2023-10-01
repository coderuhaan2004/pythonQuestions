def mergesort(a):
    if len(a)<=1: #if length of array is 1 or less, return the array
        return a
    else:
        mid = len(a)//2
        left = mergesort(a[:mid]) #recursively sort the left half
        right = mergesort(a[mid:]) #recursively sort the right half
        return merge(left,right) #merge the two halves

def merge(left,right):
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):#while both halves have elements
        if left[i]<=right[j]: #if the left element is smaller, append it to the result
            result.append(left[i])
            i+=1
        else: #if the right element is smaller, append it to the result
            result.append(right[j])
            j+=1
    result += left[i:] #append the rest of the left half
    result += right[j:] #append the rest of the right half
    return result

arr = [5,4,3,2,1]
print(mergesort(arr))



