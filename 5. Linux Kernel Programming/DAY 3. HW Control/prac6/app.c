#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <signal.h>

#define NOD_NAME "/dev/deviceFile"

void btn_interrupt(int signum){
    for(int i=0; i<3; i++){
	printf("PRESSED!\n");
    }
}

int main(){
    signal(SIGIO, btn_interrupt);
    
    int fd = open(NOD_NAME, O_RDWR);
    if( fd<0 ){
        printf("ERROR\n");
        exit(1);
    }	

    int pid = getpid();
    ioctl(fd, _IO(0,3), pid);
    printf("Start! pid : %d\n", pid);
    
    while(1){	
	printf("====HI====\n");
	usleep(300*1000);	
    }

    printf("End!\n");
    close(fd);
    return 0;
}
