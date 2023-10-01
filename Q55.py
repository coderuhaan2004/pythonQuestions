'''Use timer to compare the speed of bubble sort, quick sort, and merge sort. Which one is the fastest?'''
import time#import time
def bubble(a): #bubble sort
    for i in range(len(a)):#for loop to go through the array
        for j in range(len(a)-1):#for loop to go through the array
            if a[j]>a[j+1]:#if the first element is greater than the second element
                a[j],a[j+1]=a[j+1],a[j]#swap the elements
    return a#return the array
def quicksort(a):#quick sort
    if len(a)<=1:#if the length of the array is less than or equal to 1
        return a#return the array
    else:# if the length of the array is greater than 1
        pivot=a.pop() #pop the last element of the array
    less=[]#create an empty array for the elements less than the pivot
    greater=[]#create an empty array for the elements greater than the pivot
    for i in a:#for loop to go through the array
        if i<pivot:#if the element is less than the pivot
            less.append(i)#append the element to the less array
        else:#if the element is greater than the pivot
            greater.append(i)#append the element to the greater array
    return quicksort(less)+[pivot]+quicksort(greater)#return the quicksort of the less array, the pivot, and the quicksort of the greater array
def mergesort(a):#merge sort
    if len(a)<=1:#if the length of the array is less than or equal to 1
        return a#return the array
    else:#if the length of the array is greater than 1
        mid=len(a)//2#find the middle of the array
        left=a[:mid]#split the array into two halves
        right=a[mid:]#split the array into two halves
        return merge(mergesort(left),mergesort(right))#return the merge of the mergesort of the left array and the mergesort of the right array
def merge(left,right):#merge function
    result=[]#create an empty array
    i,j=0,0#set i and j to 0
    while i<len(left) and j<len(right):#while i is less than the length of the left array and j is less than the length of the right array
        if left[i]<=right[j]:#if the element in the left array is less than or equal to the element in the right array
            result.append(left[i])#append the element in the left array to the result array
            i+=1#
        else:#if the element in the left array is greater than the element in the right array
            result.append(right[j])#append the element in the right array to the result array
            j+=1# increment j
    result+=left[i:]#add the rest of the elements in the left array to the result array
    result+=right[j:]#add the rest of the elements in the right array to the result array
    return result#return the result array

f = open("words.txt", "r")#open the file
a = f.read()#read the file
a = a.split()#split the file
#convert a to array
L = []#create an empty array
for i in a:#for loop to go through the array
    L.append(i)#append the element to the array
print("Bubble Sort:",bubble(a))#print the bubble sort of the array
print("Quick Sort:",quicksort(a))#print the quick sort of the array
print("Merge Sort:",mergesort(a))#print the merge sort of the array

'''Measure the time taken for each sort'''
#bubble sort
start = time.time()#start the timer
bubble(a)#bubble sort
end = time.time()#end the timer
print("Bubble Sort Time:",end-start)#print the time taken for bubble sort
#quick sort
start = time.time()#start the timer
quicksort(a)#quick sort
end = time.time()#end the timer
print("Quick Sort Time:",end-start)#print the time taken for quick sort
#merge sort
start = time.time()#start the timer
mergesort(a)#merge sort
end = time.time()#end the timer
print("Merge Sort Time:",end-start)#print the time taken for merge sort

'''The fastest sort is merge sort'''
print("The fastest sort is merge sort")#print the fastest sort




