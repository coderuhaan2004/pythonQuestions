def is_prime(n):#function to check prime
    isprime = True#initially isprime is true
    for i in range(2,int((n/2))+1): #loop to check prime
        if n ==0:#if n is 0 then isprime is false
            isprime = False#isprime is false
        if n==1:#if n is 1 then isprime is false
            isprime = False#isprime is false
        if n ==2:#if n is 2 then isprime is true
             isprime = True#isprime is true
        if(n%i==0):#if n is divisible by i then isprime is false
            isprime = False#isprime is false
        if isprime:#if isprime is true then return n
            return n#return n
a = int(input('Enter the number: '))#input from user
for i in range(2,a+1):#loop to print prime numbers
    print(is_prime(i))#print prime numbers

        
