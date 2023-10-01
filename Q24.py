n = float(input('Enter the temperature: '))#input the temperature
print("Type 1 if you want to convert it to degree celsius")#input the type of conversion
print("Type 2 if you want to convert it to degree fahrenheit")#input the type of conversion
a = int(input())#input the type of conversion
b=0#initializing the variable
if(a==1):#if you want to convert the input to degree celsius
    b=((a-32)*5)/9#converting the input to degree celsius
if(a==2):#if you want to convert the input to degree fahrenheit
    b=a*(9/5)+32#converting the input to degree fahrenheit
print(b)#printing the output


