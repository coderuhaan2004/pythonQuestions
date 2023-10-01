def curve(n,c):
    # we use idea of coordinate geometry that y^2 = ax
    x =int(n/2)
    #calculate maximum value of function for y coordinate
    max = int(((x**2)*abs(c)/4))
    # if curve is positive print straight parabola
    if c >= 0:
        for i in range(0,n):
            #print the value of star pattern
            pattern = int((((x-i)**2)*abs(c)/4))
            print((pattern)*" "+ "*")
    else:
        #if curve is negative do the latter
        for i in range(0,n):
            var = int((((x-i)**2)*abs(c)/4)) #x-i is used to displace the curve by some units
            print((max-var)*" "+ "*") #prints inverted pattern


val = int(input("Enter a number : ")) #takes input
v = float(input("Enter the curve : ")) #takes input

curve(val , v*10)
