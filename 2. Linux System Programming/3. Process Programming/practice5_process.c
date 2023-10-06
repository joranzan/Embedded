#include <stdio.h>
#include <signal.h>
#include <unistd.h>

void run(int num){
    printf("HO!\n");
}

int main(){
    signal(SIGUSR1, run);
	
    pid_t pid = getpid();
    printf("My PID : %d\n", pid);

    while(1) {
	printf("HAHIHUHEHO!\n");
	sleep(1);
    }
    return 0;
}
