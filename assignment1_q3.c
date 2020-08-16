#include <stdio.h>

int main() {
	int i;
	int n;
	float sum = 1;
	int check = 1;

	printf("Enter a positive number n to find the sum 1+1/2+...+1/n: "); 
	scanf("%d", &n);

	if (n == 1){
		printf("sum = 1");
	}


	else {
		printf("sum = 1 + ");
		for (i = 2; i <= n; ++i){
        		if((sum + 1/(float)i)<(sum + 0.001)){
            			printf("\n\n\nCondition: Sum value changed by value less than 0.001. Summation halted.\n");
            			check = 0;
            			break;
			}
			sum = sum + 1/(float)i;
			if(i<n){
				printf("1/%d + ", i);
			}
			else{
				printf("1/%d", i);
			}
		}
    		if(check == 1){
			printf(" = %.2f", sum);
		}
	}


	return 0;
}