# question=Write a program that takes 2 Matrices as input and prints the matrix sum of them.
# Input=2 matrices.
# Output= Print the matrix sum of these 2 matrices

# code for this question

X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

result = [[X[i][j] + Y[i][j] for j in range
           (len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)