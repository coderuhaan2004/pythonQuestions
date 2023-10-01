n = int(input('Enter the decimal number: '))#taking input
binary = ""#taking empty string
while (n>0):#looping until n is greater than 0
    r = n%2#taking remainder
    binary = binary + str(r)#adding remainder to the string
    n= n//2#dividing n by 2
rev = "" #taking empty string
for i in range(0,len(binary)):#looping through the length of binary
    rev += binary[len(binary)-i-1]#reversing the digits of binary according to the method
print(rev)#printing the reversed binary number


