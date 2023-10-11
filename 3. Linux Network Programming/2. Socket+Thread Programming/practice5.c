#include <stdio.h>
#include <time.h>

int main(){

	clock_t a = clock();
	printf("%ld, %ld\n", a, CLOCKS_PER_SEC );	

	return 0;
}
