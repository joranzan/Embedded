#include<stdio.h>
#include<signal.h>
#include<stdlib.h>
#include<unistd.h>


void gogo(){
	printf("SYSTEM ERROR\n");
	exit(1);
}


int main(){

	signal(SIGALRM, gogo);

	
	while(1) {
	
		printf("INPUT >> ");
		
		alarm(3);

		char c[5];
		scanf("%s",c);

		printf("%s\n",c);

	}

}
