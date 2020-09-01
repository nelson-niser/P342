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
        B[k] = B[k] / pivot

        # A[y][z] --> 0 ; y != z
        for j in range(n):
                if A[j][k] == 0 or j == k:
                    continue
                else:
                    temp = A[j][k]
                    for i in range(n):
                        A[j][i] = A[j][i] - temp * A[k][i]
                    B[j] = B[j] - temp * B[k]

    return B


#########################   Q1   ##################################

# q1 A
with open('q1_A.txt') as q1_A:
   A = [[int(num) for num in row.split(' ')] for row in q1_A]

# q1 D
with open('q1_D.txt') as q1_D:
    for row in q1_D:
        B = [float(num) for num in row.split(' ')]

# Compute X
X = gaussJordan(A, B)
        
print("q1) X = ", X)

##########################   Q2    ################################

# q2 A
with open('q2_A.txt') as q2_A:
    A = [[int(num) for num in row.split(' ')] for row in q2_A]
# q2 D
with open('q2_D.txt') as q2_D:
    for row in q2_D:
        B = [float(num) for num in row.split(' ')]

# Compute X
X = gaussJordan(A, B)
    
print("q2) X = ", X)



###################    END RESULT    ###################

# q1) X = [3.0, 1.0, -2.0]
# q2) X = [-2.0, -2.0, 1.0]