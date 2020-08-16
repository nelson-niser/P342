x = input("Enter a number n to find the factorial of n: ")
factorial = 1

if(int(x)<0):
    print("You have entered a negative number.")
elif(int(x) == 0):
    print("0! = 1")
else:
    print(str(x) + "! = ", end = '')
    for i in range(1, int(x)+1):
        factorial = factorial * i
        if(i<int(x)):
            print(str(i) + " X ", end = '')
        else:
            print(i, end = '')
    print(" = " + str(factorial))

