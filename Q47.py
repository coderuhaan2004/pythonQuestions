# Input for the dimension of the matrix
dim = int(input('Enter the dimension: '))
mat1 = [] # First matrix
mat2 = [] # Second matrix
print('Enter the elements of the first matrix: ')
for i in range(dim):    # Loop to iterate through rows
    row = []    # List to store the elements of the row
    for j in range(dim):   # Loop to iterate through columns
        row.append(int(input()))    # Appending the elements to the row
    mat1.append(row)    # Appending the row to the matrix
print('Enter the elements of the second matrix: ')
for i in range(dim):    # Loop to iterate through rows
    row = []    # List to store the elements of the row
    for j in range(dim):   # Loop to iterate through columns
        row.append(int(input()))    # Appending the elements to the row
    mat2.append(row)    # Appending the row to the matrix

def multiply(mat1, mat2, dim):  # Function to multiply the matrices
    mat3 = [[0, 0], [0, 0]] # Resultant matrix
    for i in range(dim):    # Loop to iterate through rows
        for j in range(dim):   # Loop to iterate through columns
            for k in range(dim): #Loop to follow the formula of matrix multiplication
                mat3[i][j] += mat1[i][k] * mat2[k][j] # Formula for matrix multiplication
    return mat3 # Returning the resultant matrix
print(multiply(mat1, mat2, dim))# Printing the resultant matrix
