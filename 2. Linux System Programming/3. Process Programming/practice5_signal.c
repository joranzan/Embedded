#include <stdio.h>
#include <signal.h>
#include <sys/types.h>
#include <stdlib.h>

int main() {
    //gogo 를 먼저 실행해서 pid를 확인 한 뒤 수정해서 빌드한다.
    pid_t target_pid = 6639;

    int ret = kill(target_pid, SIGUSR1);

    if (ret == 0) {
        printf("%d <- signal transmit!\n", target_pid);
    } 
    else {
        printf("Fail!\n");
	exit(1);
    }

    return 0;
}
