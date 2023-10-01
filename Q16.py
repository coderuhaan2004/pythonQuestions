n = input('Enter the string: ')#input the string
c = 0#initialise number of consonants to 0
v = 0#initialise number of vowels to 0

for i in range(0,len(n)):#for loop to check each letter
    if(n[i] in ["a","e","i","o","u"]):#if any letter is equal to a,e,i,o,u
        v= v+1# increase number of vowels by 1
    else: #if it is not vowel
        c = c+1#increase number of consonants by 1
print("It has",(v),"vowels,")#print number of vowels
print("It has",(c),"consonants.")#print number of consonants



