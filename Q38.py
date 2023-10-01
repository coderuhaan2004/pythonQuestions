def is_even(n): #function to check if a number is even or not
    if n % 2 == 0:#if the number is divisible by 2 then it is even
        return True#return true if the number is even
    else:#if the number is not divisible by 2 then it is odd
        return False #return false if the number is odd
a = int(input("Enter a number: "))#input a number
print(is_even(a))#print the result
