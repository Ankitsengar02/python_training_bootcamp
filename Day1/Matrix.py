matrix1=[[5,5,5],[5,5,5],[5,5,5]]
matrix2=[[5,5,5],[5,5,5],[5,5,5]]
#addition
addition=[]

for i in range(len(matrix1)):
    row=[]
    for j in range(len(matrix1[0])):
        sum_value = matrix1[i][j] + matrix2[i][j]
        row.append(sum_value)
    addition.append(row)

print("Addition of matrix:")
for row in addition:
    print(row)

#substraction
substraction = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        sub_value = matrix1[i][j] - matrix2[i][j]
        row.append(sub_value)
    substraction.append(row)

print("Result Matrix:")
for row in substraction:
    print(row)

#Multiplication
multi =[]
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix2[0])):
        sum_value = 0
        for k in range(len(matrix2)):
            sum_value += matrix1[i][k] * matrix2[k][j]
        row.append(sum_value)
    multi.append(row)

print("Result Matrix:")
for row in multi:
    print(row)

