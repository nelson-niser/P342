#include <stdio.h>

int main() {
	int i;
	int n;
	int factorial = 1;

	printf("Enter a number n to find the factorial of n: "); 
	scanf("%d", &n);

	if (n<0){
		printf("You have entered a negative number.");
	}

	else if (n == 0){
		printf("0! = 1");
	}

	else {
		printf("%d! = ", n);
		for (i = 1; i <= n; ++i){
			factorial = factorial * i;
			if(i<n){
				printf("%d X ", i);
			}
			else{
				printf("%d", i);
			}
		}
		printf(" = %d", factorial);
	}

	return 0;
}