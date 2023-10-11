#include <stdio.h>
#include <time.h>
int main(){

	time_t time1 = time(NULL);
	printf("time1 : %ld\n", time1);
	
	time_t time2;
	time(&time2);
	printf("time2 : %ld\n", time2);

	return 0;
}
