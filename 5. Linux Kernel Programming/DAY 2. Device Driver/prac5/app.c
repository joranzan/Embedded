//read() system call 을 devicefile 로 보내는 샘플 코드

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
	printf("read Data : %s\n", buf);

	close(fd);
		
	return 0;
}
