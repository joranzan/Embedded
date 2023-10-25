//open() , close() syscall을 /dev/deviceFile 로 보내는 app 샘플 코드

#include<stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>

#define NOD_NAME "/dev/deviceFile"

int main(){
	int fd = open(NOD_NAME, O_RDWR);
	if( fd<0 ){
		printf("ERROR\n");
		exit(1);
	}
	
	char buf[100];
	read(fd, &buf, 100);	
//	printf("app msg : %s\n", buf);

	close(fd);
		
	return 0;
}
