def mirror(s): # mirror of a string
    a = ''     #empty string
    for i in range(0,len(s)):#for loop to check each character
        if s[i] == 'u':#if the character is u then add d to the empty string
            a+='d'#add d to the empty string
        elif s[i]=='r':#if the character is r then add l to the empty string
            a+='r'#add r to the empty string
        elif s[i]=='d':#if the character is d then add u to the empty string
            a+='u'#add u to the empty string
        elif s[i]=='u':#if the character is u then add d to the empty string
            a+='d'#add d to the empty string
    return a#return the string
def rev(s):#reverse of a string
    a = ''#empty string
    for i in range(0,len(s)):#for loop to check each character
        if s[i] == 'd':#if the character is d then add u to the empty string
            a+='u'#add u to the empty string
        elif s[i] == 'u':#if the character is u then add d to the empty string
            a+='d'#add d to the empty string
        elif s[i] == 'r':#if the character is r then add l to the empty string
            a+='l'#add l to the empty string
        elif s[i] == 'l':#if the character is l then add r to the empty string
            a+='r'#add r to the empty string
    return a#return the string

def peano(n):#peano curve
    if n==1:#base case
        return 'urdru'#return the string
    else:#recursive case
        return peano(n-1)+'u'+rev(mirror(peano(n-1)))+'u'+peano(n-1)+'r'+mirror(peano(n-1))+'d'+rev(peano(n-1))+'d'+mirror(peano(n-1))+'r'+peano(n-1)+'u'+rev(mirror(peano(n-1)))+'u'+peano(n-1)#use the following formula to get the peano curve

n = int(input('Enter n: '))#ask the user for the value of n
print(peano(n))#print the peano curve
l = peano(n)#assign the peano curve to a variable
x=0#x coordinate
y=0#y coordinate
L = [(0,0)]#list of coordinates
for i in range(0,len(l)):#for loop to check each character
    if l[i]=='u':#if the character is u then add (x,y+1) to the list
        L.append((x,y+1))#add (x,y+1) to the list
        y+=1#increase the y coordinate by 1
    elif l[i]=='r':#if the character is r then add (x+1,y) to the list
        L.append((x+1,y))#add (x+1,y) to the list
        x+=1#increase the x coordinate by 1
    elif l[i]=='d':#if the character is d then add (x,y-1) to the list
        L.append((x,y-1))#add (x,y-1) to the list
        y-=1#decrease the y coordinate by 1
    elif l[i]=='l':#if the character is l then add (x-1,y) to the list
        L.append((x-1,y))#add (x-1,y) to the list
        x-=1#decrease the x coordinate by 1
print(L)#print the list of coordinates









