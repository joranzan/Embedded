//write() syscall 을 사용해서 device driver 로 data 를 전송하는 app 샘플 코드

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define NOD_NAME "/dev/deviceFile"

int main(){
	int fd = open(NOD_NAME, O_RDWR);
	if( fd<0 ){
		printf("ERROR\n");
		exit(1);
	}
	
	char buf[100] = "KFC GOOD!!\n";
	write(fd, &buf, strlen(buf));
	printf("trasfer Data\n");

	close(fd);
		
	return 0;
}
