def is_palindrome(a):# function to check if the string is a palindrome
    is_palin = True #initializing it to be true
    for i in range(0,len(a)):# loop to check if the string is a palindrome
        if(a[i] !=a[len(a)-i-1]):# if first letter is equal to the last letter and so on, it is a palindrome
            is_palin = False# if not, it is not a palindrome
    if is_palin:# if it is a palindrome, print it is a palindrome
        print("It is a palindrome!")
    else:# if not, print it is not a palindrome
        print("It is not a paindrome.")# print the result
b = input('Enter the string: ')# input the string
is_palindrome(b)# perform the function
