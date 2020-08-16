# Matrix M
with open('matrix_M.txt') as matrix_M:
    M =[]
    for line in matrix_M:
        M.append([int(x) for x in line.split()])
print("M =",M)

# Matrix N
with open('matrix_N.txt') as matrix_N:
    N =[]
    for line in matrix_N:
        N.append([int(x) for x in line.split()])
print("N = ",N)



val = 0

# MxA
A = [4,2,6]
print('A = ', A)
B = []

for i in range(len(M)):
    for k in range(len(M[0])):
        val += M[i][k]*A[k]
    B.append(val)
    val = 0

print("M x A = ",B)

# MxN
C = []
row = []

for i in range(len(M)):
    for j in range(len(N[0])):
        for k in range(len(M[0])):
            val += M[i][k]*N[k][j]
        row.append(val)
        val = 0
    C.append(row)
    row = []

print("M x N = ",C)

