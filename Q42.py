def find_max(a):# function to find max value in a list
    max =-1# initial value
    for i in range(0,len(a)):# loop to find max value
        if(a[i]>max):# if value is greater than max
            max = a[i]# assign value to max
    return max# return max value
n = []# empty list
while(len(n)<10):# loop to take input
    n.append(int(input()))# append input to list
print("The max number is: ",find_max(n))# call function
