#include <stdio.h>
#include <time.h>

int main(){
    clock_t start,end;
	
	long num1 = 1;
  
    start = clock();
	for(int i=0;i<100000000;i++) num1 = (num1 << 1);
	end = clock();
	
    printf("[<< time : %lfs]\n", (float)(end-start)/CLOCKS_PER_SEC);


	long num2 = 4000000000;
	start = clock();
	for(int i=0;i<100000000;i++) num2 = num2 % 2;
	end = clock();

    printf("[%% time : %lfs]\n", (float)(end-start)/CLOCKS_PER_SEC);

    return 0;
}
