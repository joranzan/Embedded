#include<stdio.h>
#include<unistd.h>
#include<signal.h>
#include<stdlib.h>

//default : A to Z  , Z to A (0.1s)

void func(){

	char c = 'A';
	int toggle = 0;

	while(1){
		printf("%c ", c);
	
		if(toggle == 0){
			c=c+1;
			if(c=='Z') toggle= 1;
		}		
	
		else if(toggle==1){
			c=c-1;
			if(c=='A') toggle = 0;

		}	

		usleep(100*1000);
	}

}

void usr1(){
	printf("\n[Button Clicked]\n");
}

void usr2(){
	system("clear");
	printf("RESET\n");

}

void byebye(){

	printf("\nBYE\n");
	exit(0);

}

int main(){

	setbuf(stdout, NULL);

	signal(SIGUSR1, usr1);
	signal(SIGUSR2, usr2);
	signal(SIGTERM, byebye);
	
	pid_t pid = getpid();
	printf("My PID :  %d\n", pid);

	
	func();

	return 0;
}
