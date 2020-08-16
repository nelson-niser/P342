x = input("Enter a positive integer n to find the sum of integers from 1 to n: ")
sum = 0
print("sum = ", end = '')
for i in range(1, int(x)+1):
    sum = sum + i
    if(i<int(x)):
        print(str(i) + " + ", end = '')
    else:
        print(i, end = '')
print(" = " + str(sum))
