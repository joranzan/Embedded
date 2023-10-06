#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int t;
int g = 32;
int main(){
	int q=31;
	
	pid_t pid = getpid();
	printf("PID : %d\n", pid);
	while(1){
		printf(".data(%d) = %llX\n", g, &g);
		printf(".bss      = %llX\n", &t);
		printf(".heap     = %llX\n", (int*)malloc(4));
		printf(".stack    = %llX\n", &q);
		printf("======================================\n");
		sleep(1);
		g++;
	}

	return 0;
}
