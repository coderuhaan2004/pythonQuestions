a = int(input('Enter the first number: '))#inputs the first number
d = int(input('Enter the common difference: '))#inputs the common difference
b = int(input('Enter the last number: '))#inputs the last number
r = int(((b-a)/d)+1)#calculates the number of terms
for i in range(1,r+1):#loops through the number of terms
	print(a+ (i-1)*d)#prints the terms




