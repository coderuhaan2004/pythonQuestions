n = int(input('Enter the number'))#taking input from user
is_prime = True#initializing the variable
for i in range(2,int(n/2+1)):#looping from 2 to n/2
    if(n%i==0):#checking if the number is divisible by any number
        is_prime = False #changing the value of is_prime to false
if is_prime:#checking if the value of is_prime is true
    print(n,"is a prime number")#printing the result
else:#if the value of is_prime is false
    print(n,"is not a prime number")#printing the result

