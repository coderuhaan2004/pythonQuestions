def avg(a):#created the function to calculate the average of numbers
    sum = 0#initializing the sum to 0
    average = 0#initializing the average to 0
    for i in a:#for loop to calculate the sum of numbers
        sum = sum +i#adding the numbers
    average = sum/len(a)#calculating the average
    return average#returning the average
marks = []#creating an empty list
for i in range(0,5):#for loop to take input from the user
    marks.append(float(input()))#appending the input to the list
n = avg(marks)#calling the function
if n>=90:# if average is greater than or equal to 90
    print("A")#printing A
elif n in range(80,91):#if average is greater than or equal to 80 but less than 91
    print("B")#printing B
elif n in range(70,81):#if average is greater than or equal to 70 but less than 81
    print("C")#printing C
elif n in range(60,71):#if average is greater than or equal to 60 but less than 71
    print("D")#printing D
else:#if average is less than 60
    print("F")#printing F

