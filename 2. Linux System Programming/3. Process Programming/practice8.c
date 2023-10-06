#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

void gogo(){
    printf("WAKE UP!\n");
    exit(1);
}

int main(){
    signal(SIGALRM, gogo);

    printf("3 seconds\n");
    alarm(3);
    printf("wait....\n");

    while(1) sleep(1); //process die.. SEGFAULT Error

    return 0;
}
