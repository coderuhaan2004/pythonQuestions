def clockwise(s):   #function written to turn the path clockwise    
    a=''            #taking an empty string
    for i in s:     #for loop to check the direction
        if i=='D':  #if the direction is down then it will turn left
            a+='L'  #add L to the string
        elif i=='R':#if the direction is right then it will turn down
            a+='D'  #add D to the string
        elif i=='U':#if the direction is up then it will turn right
            a+='R'  #add R to the string
        elif i=='L':#if the direction is left then it will turn up
            a+='U'  #add U to the string
    return a        #return the string

def anticlockwise(s):   #function written to turn the path anticlockwise
    a=''                #taking an empty string
    for i in s:         #for loop to check the direction
        if i=='D':      #if the direction is down then it will turn right
            a+='R'      #add R to the string
        elif i=='R':    #if the direction is right then it will turn up
            a+='U'      #add U to the string
        elif i=='U':    #if the direction is up then it will turn left
            a+='L'      #add L to the string
        elif i=='L':    #if the direction is left then it will turn down
            a+='D'      #add D to the string
    return a            #return the string

def reverse(s):         #function written to reverse the path
    a=''                #taking an empty string
    for i in s:         #for loop to check the direction
        if i=='D':      #if the direction is down then it will turn up
            a+='U'      #add U to the string
        elif i=='U':    #if the direction is up then it will turn down
            a+='D'      #add D to the string
        elif i=='R':    #if the direction is right then it will turn left
            a+='R'      #add R to the string
        elif i=='L':    #if the direction is left then it will turn right
            a+='L'				#add L to the string
            					# RDL + D + DRU + R + DRU + U + LDR (pattern observed in second order SFC)
    return a            #return the string

def sfc(n):             #function written to generate the SFC
    if n==1:            #base case
        return 'DRU'    #return the string
    else:               #recursive case
        return (reverse(anticlockwise(sfc(n-1)))+'D'+sfc(n-1)+'R'+sfc(n-1)+'U'+reverse(clockwise(sfc(n-1)))) #return the string following some pattern
n=int(input("Enter a number"))  #taking input from the user
print(sfc(n))                   #printing the SFC
c = [1,1]               #initializing the coordinates
a = [[1,1]]             #initializing the list
for i in sfc(n):        #for loop to check the direction
    if i=='D':          #if the direction is down then it will add 1 to the row element 
        c[0]+=1         #add 1 to the row element
        a.append(c[:])  #append the coordinates to the list
    elif i=='U':        #if the direction is up then it will subtract 1 from the row element
        c[0]-=1         #subtract 1 from the row element
        a.append(c[:])  #append the coordinates to the list
    elif i=='R':        #if the direction is right then it will add 1 to the column element
        c[1]+=1         #add 1 to the column element
        a.append(c[:])  #append the coordinates to the list
    elif i=='L':        #if the direction is left then it will subtract 1 from the column element
        c[1]-=1         #subtract 1 from the column element
        a.append(c[:])  #append the coordinates to the list
print(a)                #printing the list






