#include<stdio.h>
#include<unistd.h>
#include<signal.h>
#include<sys/types.h>
#include<stdlib.h>
#include<string.h>


pid_t target_pid;

void gogo(){

	printf("\nTime Over\n");	
	int ret = kill(target_pid, SIGTERM);
	exit(0);
	
}

int main(int argc, char* argv[]){
	
	signal(SIGALRM, gogo);

	target_pid = atoi(argv[1]);

	while(1){
		
		printf("User Input >> ");
		alarm(7);

		char cmd[5];
		scanf("%s", cmd);


		if(strcmp(cmd,"1")==0) //SIGUSR1
		{
			int ret = kill(target_pid, SIGUSR1);
			if(ret==0) printf("Signal Transmission Succeed\n");
			else{
				printf("FAIL\n");
				exit(1);
			}
		}

		else if(strcmp(cmd,"2")==0) //SIGUSR2
		{
			int ret = kill(target_pid, SIGUSR2);
			if(ret==0) printf("Signal Transmission Succeed\n");
			else{
				printf("FAIL\n");
				exit(1);
			}

		}
		else if(strcmp(cmd,"3")==0){//SIGTERM
			int ret = kill(target_pid, SIGTERM);
			if(ret==0) printf("Signal Transmission Succeed\n");
			else{
				printf("FAIL\n");
				exit(1);

			}
		}
		else if(strcmp(cmd, "exit")==0) //EXIT
		{
			printf("Person App Exit\n");
			exit(0);

		}
		else{

			printf("INVALID COMMAND\n");
	
		}
	}
	return 0;
}
