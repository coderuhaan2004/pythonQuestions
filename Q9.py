n = int(input('Enter the number: '))#takes the input from user
i = int(input('Tables from: '))#takes the input from user for starting table
j = int(input('Tables to: '))#takes the input from user for ending table
for a in range(i,j+1):#for loop for printing the tables
    print(n,"x",a,"=",n*a)#prints the tables

