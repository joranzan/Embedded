#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){
	//부모프로세스가 혼자 있다
	//fork()가 실행되면 자식 프로세스가 생성됨
	pid_t child_pid = fork();

	if( child_pid>0 ){
		//parent
		printf("I'm Parent! I'm Busy!!\n");
		while(1);//부모는 바쁨
	}
	else if( child_pid==0 ){
		//child
		printf("HI! I'm baby! ByeBye\n");
		//Die
	}

	return 0;
}
