import numpy as np

n = int(input("What's the order of square matrix : "))

print("Enter the matrix elements row wise:")
elements = []
for i in range(n):
    row = list(map(int, input().split()))
    elements.append(row)

matrix = np.array(elements)

diag_sum = 0
for i in range(n):
    diag_sum += matrix[i][i]

print("Matrix:")
print(matrix)
print("Sum of diagonal elements:", diag_sum)
