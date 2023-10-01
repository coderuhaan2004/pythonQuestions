#function for adding to square matrices
def add(l1,l2,dim):#l1 and l2 are the two matrices and dim is the dimension of the matrix
    l3 = [] #l3 is the matrix which will store the sum of the two matrices
    for i in range(dim): #loop for the rows
        l3.append([]) #appending an empty list to l3
        for j in range(dim): #loop for the columns
            l3[i].append(l1[i][j]+l2[i][j]) #adding the elements of the two matrices and appending it to l3
    return l3   #returning the sum matrix
mat1 = []  #mat1 is the first matrix
mat2 = []  #mat2 is the second matrix
dim = int(input("Enter the dimension of the matrix: ")) #inputting the dimension of the matrix
print("Enter the elements of the first matrix: ")#inputting the elements of the first matrix
for i in range(dim): #loop for the rows
    mat1.append([])#appending an empty list to mat1
    for j in range(dim):#loop for the columns
        mat1[i].append(int(input()))#inputting the elements of the matrix
print("Enter the elements of the second matrix: ")#inputting the elements of the second matrix
for i in range(dim):#loop for the rows
    mat2.append([])#appending an empty list to mat2
    for j in range(dim):#loop for the columns
        mat2[i].append(int(input()))#inputting the elements of the matrix
print("The sum of the two matrices is: ")#printing the sum of the two matrices
print(add(mat1,mat2,dim))#printing the sum of the two matrices

