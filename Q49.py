print("Make sure you have a file named output.txt in the same directory as this file.")
def read():#function to read a file
    file = open('output.txt','r')#open the file in read mode
    num = file.read()#read the file
    file.close() #it is a good practise to close a file.
    return num #it is important to return and not a print a variable which is inside the function.
contents = read()#call the function
print(contents)#print the contents of the file
