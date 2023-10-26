#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h> //ioctl 사용을 위한 header

#define NOD_NAME "/dev/deviceFile"

int main(){
    // /dev/deviceFile 을 read/write 로 열기, fops의 .open 실행
    int fd = open(NOD_NAME, O_RDWR);
    if( fd<0 ){
        printf("ERROR\n");
        exit(1);
    }
	
	while(1){
		unsigned long input;
		unsigned int  cmd;
		printf("command : 3~6, Age, Birth(Month, Day), Phone Number\n");
		scanf("%d %lu", &cmd, &input);
    	//ioctl로 /dev/deviceFile 에 _IO() 매크로로 arg 값 전달
		
	    int ret = ioctl(fd, _IO(0,cmd), input);

   		 //ioctl 의 return 값으로 error 검출
    	if(ret < 0){
       		 printf("command range error\n");
			 break;
   		 }
	}

    close(fd);
    return 0;
}
