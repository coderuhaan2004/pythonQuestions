import string
d = {
    'a':'z',
    'b':'y',
    'c':'x',
    'd':'w',
    'e':'v',
    'f':'u',
    'g':'t',
    'h':'s',
    'i':'r',
    'j':'q',
    'k':'p',
    'l':'o',
    'm':'n',
    'n':'m',
    'o':'l',
    'p':'k',
    'q':'j',
    'r':'i',
    's':'h',
    't':'g',
    'u':'f',
    'v':'e',
    'w':'d',
    'x':'c',
    'y':'b',
    'z':'a'
}
f = open("english_random.txt", "r")   #First open the file 
r = f.read()                    #Read the file

def textstrip(r):               #Function to strip the text
    a = ''                      #Empty string
    for i in r:                 #For loop to check if the character is in the alphabet  
        if (i in 'abcdefghijklmnopqrstuvwxyz'): #If the character is in the alphabet, add it to the empty string
            a += i              #Add the character to the empty string
    return a                   #Print the string

def letter_distribution(r):
    a = textstrip(r)
    b = {}                      #Empty dictionary
    for i in a:
        if(i in b):             #If the character is in the dictionary, add 1 to the value
            b[i] += 1
        else:                   #If the character is not in the dictionary, add it to the dictionary
            b[i] = 1
    return b

def substitution_encrypt(r,d):
    a = ''
    for i in r:
        if(i in d):
            a += d[i]
    return a

def substitution_decrypt(r,d):
    a = substitution_encrypt(r,d)
    b = ''
    for i in a:
        if(i in d):
            b += d[i]
    return b

def cryptanalyse_substitution(r):
    a = textstrip(r)
    b = substitution_encrypt(r,d)
    e = {}
    for i in a:
        for j in range(len(b)):
            e[i] += b[j]
            if(i in e):
                break
# stop iterating through the string when all the charactersare in dictionary at least once
    return e

def vignere_encrypt(r,password):#given a password and a plaintext, encrypt the plaintext using the vignere cypher
#create vignere table #create list of alphabet
    from string import ascii_lowercase as l#alphabet
    class CypherTable:#create class
        def __init__(self):#create table
            self.table = [l[i:] + l[:i] for i in range(len(l))]#create list of alphabet shifted by one each time
    lst =[*CypherTable().table[0]]#list of alphabet
    password = password * (len(r) // len(password)) + password[:len(r) % len(password)]#repeat password until it is the same length as r
    ciphertext = ''#empty string

    for i in range(len(r)):#for each letter in r
        row = lst.index(r[i])#take first letter of r and take its index in the alphabet in the row oflist named lst
        col = lst.index(password[i%len(password)])#take first letter of password and take its index in the alphabet in the column of list named lst
        ciphertext += CypherTable().table[row][col] #add the letter at the intersection of the row and column to the ciphertext
    return ciphertext #return ciphertext
#given a password and a plaintext, encrypt the plaintext using the vignere cypher
#take first letter of r and take its index in the alphabet in the row oflist named lst 
#take first letter of password and take its index in the alphabet in the column of list named lst
#take the letter at the intersection of the row and column and add it to the ciphertext
#repeat for all letters in password

def vignere_decrypt(r,password):#given a password and a ciphertext, decrypt the ciphertext using the vignere cypher
#create vignere table #create list of alphabet
    from string import ascii_lowercase as l#alphabet
    class CypherTable:#create class
        def __init__(self):#create table
            self.table = [l[i:] + l[:i] for i in range(len(l))]#create list of alphabet shifted by one each time
    lst =[*CypherTable().table[0]]#list of alphabet
    password = password * (len(r) // len(password)) + password[:len(r) % len(password)]#repeat password until it is the same length as r
    plaintext = ''#empty string
    
    for i in range(len(r)):#for each letter in r
        row = lst.index(password[i])#take first letter of password and take its index in the alphabet in the row oflist named lst
        col = CypherTable().table[row].index(r[i])#take first letter of r and take its index in the alphabet in the column of list named lst
        plaintext += lst[col] #add the letter at the intersection of the row and column to the plaintext
    return plaintext #return plaintext

def rotate_compare(s,r):
    r = r%len(s) # make sure r is less than the length of the string
    t = s[r:] + s[:r] # return the string rotated by r
    counter = 0
    for i in range(len(s)):
        if(t[i] == s[i]):
            counter+=1
    return t, counter

def cryptanalyse_vignere_afterlength(ciphertext, password_length):
    from string import ascii_lowercase as l#alphabet
    class CypherTable:#create class
        def __init__(self):#create table
            self.table = [l[i:] + l[:i] for i in range(len(l))]#create list of alphabet shifted by one each time
    lst =[*CypherTable().table[0]]#list of alphabet
    password = ''#empty string
    
def cryptanalyse_vignere_findlength(r):
    '''given the string s, find out the length of the password using which some text has resulted in the string s'''
    from string import ascii_lowercase as l#alphabet
    class CypherTable:#create class
        def __init__(self):#create table
            self.table = [l[i:] + l[:i] for i in range(len(l))]#create list of alphabet shifted by one each time
    lst =[*CypherTable().table[0]]#list of alphabet
    for i in range(1, len(r)):#for each possible length of password
        counter = 0
        for j in range(len(r)):#for each letter in r
            row = lst.index(r[j])#take first letter of r and take its index in the alphabet in the row oflist named lst
            col = CypherTable().table[row].index(r[(j+i)%len(r)])#j+i is the index of the letter in the ciphertext that is i letters after the letter at index j in the ciphertext
            if(lst[col] == r[j]):#if the letter at the intersection of the row and column is the same as the letter at index j in the ciphertext
                counter += 1#add one to counter
        if(counter == len(r)):#if counter is equal to the length of the ciphertext
            return i#return i
    return 0#if no length is found, return 0

def cryptanalyse_vignere(r):
    '''given a string r, output the password as well as the plaintext'''
    from string import ascii_lowercase as l#alphabet
    class CypherTable:#create class
        def __init__(self):#create table
            self.table = [l[i:] + l[:i] for i in range(len(l))]#create list of alphabet shifted by one each time
    lst =[*CypherTable().table[0]]#list of alphabet
    password_length = cryptanalyse_vignere_findlength(r)#find the length of the password
    password = ''#empty string
    for i in range(password_length):#for each letter in the password
        counter = 0
        for j in range(len(r)):#for each letter in r
            row = lst.index(r[j])#take first letter of r and take its index in the alphabet in the row oflist named lst
            col = CypherTable().table[row].index(r[(j+i)%len(r)])#j+i is the index of the letter in the ciphertext that is i letters after the letter at index j in the ciphertext
            if(lst[col] == r[j]):#if the letter at the intersection of the row and column is the same as the letter at index j in the ciphertext
                counter += 1#add one to counter
        if(counter == len(r)):#if counter is equal to the length of the ciphertext
            password += lst[i]#add the letter at index i in the alphabet to the password
    plaintext = vignere_decrypt(r,password)#decrypt the ciphertext using the password
    return password, plaintext#return the password and the plaintext


