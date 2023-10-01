def fibo(n): #function to print nth term of fibonacci series
    farray = [1,2]#array to store fibonacci series
    for i in range(0,n-2):#loop to generate fibonacci series
        farray.append(farray[i]+farray[i+1])#appending the sum of last two terms to the array
    print(farray[n-2])#printing the nth term of the series
a = int(input('Enter the nth term: '))#taking input from user
fibo(a)#calling the function

