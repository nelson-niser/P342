#include <stdio.h>

int main() {
	int i;
	int x;
	int sum = 0;

	printf("Enter a positive integer n to find the sum of integers from 1 to n: "); 
	scanf("%d", &x);

	printf("Sum = ");
	for (i = 1; i <= x; ++i){
		sum = sum + i;
		if(i<x){
			printf("%d + ", i);
		}
		else{
			printf("%d", i);
		}
	}
	printf(" = %d", sum);
	return 0;
}