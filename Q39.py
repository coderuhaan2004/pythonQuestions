import math #importing math module to use pi
def circle_area(radius):#defining function
    return math.pi * radius ** 2#returning area of circle
r = float(input("Enter radius: "))#taking input from user
print("Area of circle:", circle_area(r))#printing area of circle
