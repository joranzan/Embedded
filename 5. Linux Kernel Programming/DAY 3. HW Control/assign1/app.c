#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>

struct Node{
	int num1;
	int num2;
	int num3;
	int num4;
};
int main(){
    int fd = open("/dev/deviceFile", O_RDWR);
    if( fd<0 ){
        printf("ERROR\n");
        exit(1);
    }
	
	while(1){

    	struct Node readData;
    	unsigned int writeData;
		printf("Four Numbers : \n");
		scanf("%d %d %d %d", &readData.num1, &readData.num2, &readData.num3, &readData.num4);
    	ioctl(fd, _IO(0,3), &readData);  //user to kernel
		
    	printf("Send 4 Numbers from User to Kernel\n");

    	ioctl(fd, _IO(0,4), &writeData);
		printf("%d\n", writeData);
    	printf("Recieve Sum of Numbers from Kernel\n");
		
		int ret = ioctl(fd, _IO(0,5), &writeData);
		if(ret < 0){

			printf("Error\n");
			break;
		}
		
	}
  close(fd);
  return 0;
}
