points = []

# Assign co-ordinates
for x in range(6):
	for y in range(6):
		points.append([x,y])

no_points = 6*6
pairs = no_points**2

total = 0

for i in range(no_points):
	x1,y1 = points[i]
	for j in range(no_points):
		x2,y2 = points[j]
		total += abs(x2 - x1) + abs(y2 - y1)


avg = total/pairs
print("The average distance between two points of 6x6 grid: ",avg)