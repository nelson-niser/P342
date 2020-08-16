#include<stdio.h>
#include<stdlib.h>
int main(){
    // Matrix M
	FILE *A;
	A = fopen("matrix_M.txt","r");
	int M[3][3];

	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
			fscanf(A,"%d*%c", &M[i][j]);
		}
	}

    printf("M :\n");
	for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
         	printf("%d ", M[i][j]);
         	if(j==2){
                printf("\n");	
    		}
    	}
	}
    
	// Matrix N 
	FILE *B;
	B = fopen("matrix_N.txt","r");
	int N[3][3];

	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
			fscanf(B,"%d*%c", &N[i][j]);
		}
	}

    printf("\nN :\n");
	for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
         	printf("%d ", N[i][j]);
         	if(j==2){
                printf("\n");	
    		}
    	}
	}

    // Vector A
    int vec_A[3][1] ={{4},{2},{6}};
    printf("\nA : ");
	for(int i=0; i<3; i++) {
      for(int j=0; j<1; j++) {
         	printf("%d ", vec_A[i][j]);
    	}
	}


	// MxA

	int Y[3][1] ={{0},{0},{0}};

	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
			for(int k=0; k<3; k++){
				Y[i][j] += M[i][k] * vec_A[k][j];
			}
		}
	}

    printf("\n\nM x A : ");
	for(int i=0; i<3; i++) {
      for(int j=0; j<1; j++) {
         	printf("%d ", Y[i][j]);
    	}
	}



	// MxN
	int X[3][3]={{0, 0, 0},{0, 0, 0},{0, 0, 0}};



	for(int i=0; i<3; i++){
		for(int j=0; j<3; j++){
			for(int k=0; k<3; k++){
				X[i][j] += M[i][k] * N[k][j];
			}
		}
	}

	printf("\n\nM x N:\n");
	for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
         	printf("%d ", X[i][j]);
         	if(j==2){
                printf("\n");	
    		}
    	}
	}
	
	
	
}