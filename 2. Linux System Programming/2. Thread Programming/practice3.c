#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void* abc(void* p){
    int a = *(int*)p;
    while(1){
        printf("%d\n", a);
        a++;
        usleep(300*1000);
	if( a>10 ) break;
    }
}

int main(){
    pthread_t tid;
    int gv = 1;
	
    pthread_create(&tid, NULL, abc, &gv);
    pthread_join(tid, NULL);
    return 0;
}
