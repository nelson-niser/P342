#include<stdio.h>
#include<stdlib.h>
int main(){
	

	int no_points = 6*6;
	float pairs = no_points *no_points ;

	float total = 0;

	// Point x co-ordinate
	for (int x1 = 0; x1 < 6; ++x1){
		// Point y co-ordinate
		for (int y1 = 0; y1 < 6; ++y1){


				for (int x2 = 0; x2 < 6; ++x2){
					for (int y2 = 0; y2 < 6; ++y2){

						total = total + abs(x1-x2) + abs(y1-y2);

					}
				}
		}
	}

	float avg = total/pairs;

	printf("The average distance is ");
	printf("%.4f",avg);

}
