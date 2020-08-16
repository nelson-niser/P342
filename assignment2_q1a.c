#include<stdio.h>
#include<stdlib.h>
int main(){
	

	int no_points = 6;
	float pairs = 6*6;

	float total = 0;
	for (int i = 0; i < no_points; ++i){
		for (int j = 0; j < no_points; ++j){
			total = total + abs(i-j);
		}
	}

	float avg = total/pairs;

	printf("The average distance is ");
	printf("%.4f",avg);

}

