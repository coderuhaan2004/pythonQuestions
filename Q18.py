def fibo(n):#function to print fibonacci series
    farray = [1,2]#initializing the array with first two elements
    for i in range(0,n-2):#loop to run from 0 to n-2
        farray.append(farray[i]+farray[i+1])#append the number in the list by adding it to last two elements of list farray
    for i in farray:
        print(i)#prints all the elements of the array

a = int(input('Enter the last number: '))#takes the input from the user
fibo(a)# performs the function

