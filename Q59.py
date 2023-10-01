import string   #importing string module
def cipher(s):  #defining function
    l = string.ascii_lowercase  #storing all lowercase letters in l
    a = ""  #empty string
    for i in s:  #for loop to iterate through string
        for j in range(0,len(l)):  #for loop to iterate through l
            if i == l[j]:  #if letter in string is equal to letter in l
            #add 3rd letter after i letter in string
                if j+3 > len(l)-1: #if index of letter + 3 is greater than length of l for example in case of z
                    a = a + l[j+3-len(l)] #add 3rd letter after i letter in string
                else:#if index of letter + 3 is less than length of l
                    a = a + l[j+3]#add 3rd letter after i letter in string
    return a #returning encrypted string
s = input('Enter the string to be encrypted: ') #taking input from user
print(cipher(s)) #printing encrypted string


