#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>

#define NOD_NAME "/dev/deviceFile"

int main(){
    int fd = open(NOD_NAME, O_RDWR);
    if( fd<0 ){
        printf("ERROR\n");
        exit(1);
    }

    int btn;
    while(1){
        int ret = ioctl(fd, _IO(0,5), &btn);
        if(ret < 0){
            printf("command invalid!\n");
            break;
        }
        printf("btn = %d\n", btn);
        if( btn==0 ){
            ioctl(fd, _IO(0,3), 0);
        }
        else{
            ioctl(fd, _IO(0,4), 0);
        }
    }

    close(fd);
    return 0;
}
