n = int(input('Enter the factorial'))#take the input
def fac(a):#define the function to find factorial
    p = 1#initialize the variable
    for i in range(2,a+1):#loop to find factorial
        p = p*i #multiply the numbers to p
    print(p)#print the factorial
fac(n)#call the function
