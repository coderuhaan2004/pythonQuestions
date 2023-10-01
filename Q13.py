def intersperse(a,b):#function to perform the task
    #make sure that a & b are of same length
    if(len(a)!=len(b)):#if length of a and b are not equal
        print("Invalid")#print invalid
    else:#else perform the task
        c = "" #take an empty string
        for i in range(0,len(a)):#loop through the length of a
            c += a[i]+b[i] #add first letter of a then first element of b and so on...
    print(c)#print the string
p = input('String 1: ')# take input of 2 strings
q = input('String2: ')#take input of 2 strings
intersperse(p,q) #perform the function
