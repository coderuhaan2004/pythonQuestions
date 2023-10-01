def partition(a,l,h):
    pivot = a[l]
    i = l
    j = h
    while(i<j):
        while(a[i]<=pivot):
            i+=1
        while(a[j]>pivot):
            j-=1
        if (i<j):
            a[i],a[j] = a[j],a[i]
    a[l],a[j] = a[j],a[l]
    return j
def quicksort(a,l,h):
    if(l<h):
        j = partition(a,l,h)
        quicksort(a,l,j)
        quicksort(a,j+1,h)
a = [10,16,8,12,15,6,3,9,5,1000]
quicksort(a,0,len(a)-1)
print(a)

    





    
