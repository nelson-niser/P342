sum = 1
check = 1
x = input("Enter a positive number n to find the sum 1+1/2+...+1/n: ") 

if(int(x) == 1):
	print("sum = 1", end="")

else:
    print("sum = 1 + ", end="")
    for i in range(2, int(x)+1):
        if((sum + 1/i)<(sum + 0.001)):
            print("\n\n\nCondition: Sum value changed by value less than 0.001. Summation halted.\n")
            check = 0
            break
        sum = sum + 1/i
        if(i<int(x)):
            print("1/" + str(i) + "+ ", end="")
        else:
            print("1/" + str(i) + " = ", end="")
    if(check == 1):
        print(sum)
