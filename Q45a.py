print("Enter the elements of 2x2 matrix 1: ")# prints the message
mat1 = [[int(input())for x in range(0,2)] for y in range(0,2)]# takes the input from the user for 1st matrix
print("Enter the elements of 2x2 matrix 2: ")# prints the message
mat2 = [[int(input())for x in range(0,2)] for y in range(0,2)]# takes the input from the user for 2nd matrix
mat3 = []# creates an empty list

for i in range(0,2):# for loop for the rows
    mat3.append([mat1[i][j]+mat2[i][j] for j in range(0,2)])# adds the elements of the 2 matrices and appends it to the empty list
for i in range(0,2):# for loop for the rows
    for j in range(0,2):# for loop for the columns
        print(mat3[i][j], end = " ")# prints the elements of the list
    print()# prints the new line

        







