n = int(input('Enter the year: '))#takes input for year
if ((n%400==0) or #if n is divisble by 400
    (n%100!=0) and#if n is not divisible by 100
    (n%4==0)): #if n is divisble by 4
    is_leap = True#then it is leap year
else:#else it is not leap year
    is_leap = False#then it is not leap year
if is_leap:#if it is leap year
    print("It is leap year.")#then print it is leap year
else:#else it is not leap year
    print("It is not leap year.")#then print it is not leap year

