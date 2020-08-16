#include<stdio.h>
int main(){

	int A[3]={4,2,6};
	int B[3]={5,4,3};
	int C[3] = {0, 0, 0};
	
	//A+B
	printf("A+B = ");
	for(int i=0; i<3; ++i){
		C[i] = A[i] + B[i];
		printf("'%d'", C[i]);
	}
	



	// AxB
	int product = 0;
	for(int i=0; i<3; ++i){
		product += A[i]*B[i];
	}
	printf("\nA.B = %d", product);

}