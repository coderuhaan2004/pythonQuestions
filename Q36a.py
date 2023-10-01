import random  #importing random module
def number(j,a):   #defining a function to count the number of times a number occurs in a list
    cj=0   #initializing a counter
    for i in range(0,1000000):  #looping through the list
        if(a[i].count(0)==j):   #checking if the number of times 0 occurs in the list is equal to the number passed to the function
            cj+=1   #incrementing the counter
    return cj   #returning the counter
p=[]    #initializing a list
for i in range(0,1000000):#looping through the list
    p.append([])    #appending an empty list to each element of the list
for i in range(0,1000000):  #looping through the list
    p[random.randint(0,999999)].append(0)  #appending 0 to a random list in the list
for i in range(0,11):#looping through the list
    print(number(i,p))  #printing the number of times 0 occurs in the list
for i in range(0,11):#looping through the list
    prob = number(i,p)/1000000  #calculating the probability
    print(prob,"for x = ",i,"") #printing the probability
    print(1/prob)   #printing the reciprocal of the probability

