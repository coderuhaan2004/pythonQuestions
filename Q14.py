def reverse(a):#defining the function
    rev = ""#initializing the variable
    for i in range(0,len(a)):#looping through the string
        rev += a[len(a)-i-1]#adding the characters to the variable
    print(rev)#printing the reversed string

b=input('Enter the string to be reversed: ')#taking the input
reverse(b) #applying the function
