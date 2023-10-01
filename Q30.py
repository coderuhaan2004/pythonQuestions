def gcd(a,b,counter=0):#counter is used to count the number of times the function is called
    if b ==0:#base case
        return counter#returning the gcd and the number of times the function is called
    else:#recursive case
        counter +=1#incrementing the counter
        return gcd(b,a%b,counter)#find gcd of b and a%b

max_steps = -1#initializing the maximum number of steps to -1
max_indices = None#initializing the maximum indices to None
n = int(input("Enter the value of digits: "))#taking input from the user
for i in range(1,10**n):#looping through all the numbers
    for j in range(1,10**n):#looping through all the numbers
        steps = gcd(i,j)#finding the gcd of i and j
        intial_steps = 1 #initial step when b is not equal to 0
        actual_steps = steps - intial_steps #initial step is subtracted from the total steps to not count the step when b is not equal to 0
        if actual_steps > max_steps:#checking if the actual steps is greater than the maximum steps
            max_steps = actual_steps#assigning the actual steps to the maximum steps
            max_indices = (i, j)#assigning the indices to the maximum indices
print("Maximum number of steps is: ",max_steps)#printing the maximum number of steps 
print("Numbers that require maximum number of steps are: ",max_indices)#printing the numbers that require maximum number of steps
        

        

