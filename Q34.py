def fac(a): #function to find factorial of a number
    pro = 1#initializing the product
    for i in range(2,n+1):#loop to find the product
        pro = pro*i#multiplying the product with the number
    print(pro)#printing the product
n = int(input('Enter the number: '))#taking the input
fac(n)#calling the function

