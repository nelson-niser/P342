# Define vectors
vector_A = [4,2,6]
vector_B = [5,4,3]

print("A = ", vector_A)
print("B = ", vector_B)

# Size of vector
size = len(vector_A)

# Vector summation
sum = []
for i in range(size):
	sum.append(vector_A[i] + vector_B[i])

print("A+B = ", sum)

# Dot product of vectors
dot_product = 0
for i in range(size):
	pro = vector_A[i]*vector_B[i]
	dot_product += pro

print("A.B = ", dot_product)