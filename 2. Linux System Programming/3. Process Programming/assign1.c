#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
	pid_t child_pid = fork();
	
	if( child_pid>0 ){
		//parent
		printf("I'm Parent! I'm Busy!!\n");
		while(1);
	}
	else if( child_pid==0 ){
		//child
		//child 자식 생성
		printf("HI! I'm baby! ByeBye\n");
		
		pid_t grandchild_pid = fork();
		

		if(grandchild_pid>0){
			//child
			printf("Grow up!\n");
			while(1);

		}	
		else if(grandchild_pid==0){
			//grandchild

			printf("I'm Groot!\n");


		}
	}

	return 0;
}
