import random#import random module
L = []#creates an empty list
for i in range(0,1000):#loop to populate the list
    L.append(random.randint(1,1000))#inserts a random number in the list L
print("List populated! Here are its elements.")#prints a message
for i in L:#loop through list
    print(i)#prints the list
