def generate_pattern(): #function to generate the pattern
    a = ''  # empty string
    i = 1   # counter
    while len(a) < 1000000:# loop to generate the pattern
        a += (2 * i - 1) * "R" + (2 * i - 1) * "U" + (2 * i) * "L" + (2 * i) * "L" # pattern
        i += 1# increment counter
    return a# return the pattern

pattern = generate_pattern()# call the function
print(pattern)  # print the pattern

