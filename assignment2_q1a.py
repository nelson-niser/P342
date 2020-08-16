points = []

#  Assign co-ordinates
for n in range(6):
	points.append(n)

total = 0
pairs = 6**2

for i in points:
	for j in points:
		total += abs(j - i)

avg = total/pairs

print("The average distance is ", avg)