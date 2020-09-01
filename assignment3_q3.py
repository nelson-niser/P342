def partialPivot(A, B):
    n = len(B)
    for i in range(n):
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if abs(A[k][i]) > abs(A[i][i]):
                    A[i], A[k] = A[k], A[i]
                    B[i], B[k] = B[k], B[i]
    return A, B


def gaussJordan(A, B):
    
    A, B = partialPivot(A, B)
    n = len(B)

    for k in range(n):
        
        # A[x][x] --> 1
        pivot = A[k][k]
        for i in range(n):
            A[k][i] = A[k][i] / pivot
            B[k][i] = B[k][i] / pivot

        # A[y][z] --> 0 ; y != z
        for j in range(n):
                if A[j][k] == 0 or j == k:
                    continue
                else:
                    temp = A[j][k]
                    for i in range(n):
                        A[j][i] = A[j][i] - temp * A[k][i]
                        B[j][i] = B[j][i] - temp * B[k][i]

    return B

def matrixMultiplication(A, B):
    Z = [[0,0,0],[0,0,0],[0,0,0]]
    for x in range(len(A)):
        for y in range(len(B[0])):
            for z in range(len(A[0])):
                Z[x][y] += A[x][z] * B[z][y]

    return Z

with open("q3_A.txt", 'r' ) as q3_A:
    A = [[int(num) for num in row.split(' ')] for row in q3_A]
    
# An image of A to check later using multiplication
with open("q3_A.txt", 'r' ) as q3_A:
    temp = [[int(num) for num in row.split(' ')] for row in q3_A]

I = [[1,0,0],[0,1,0],[0,0,1]]

X = gaussJordan(A, I)
print("\nInverse:")
for row in X:
    print(row)

print("\nCheck:")
for row in matrixMultiplication(temp, X):
    print(row)


#########################################

# Inverse:
# [-3.0, 3.0, -7.0]
# [1.0, 1.0, 0.0]
# [1.0, 0.0, 1.0]

# Check:
# [1.0, 0.0, 0.0]
# [0.0, 1.0, 0.0]
# [0.0, 0.0, 1.0]