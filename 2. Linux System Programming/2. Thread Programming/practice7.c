#include<stdio.h>
#include<pthread.h>

int cnt=0; //.data 공유되는 메모리
void* run(void* arg){
    for(int i=0; i<10000; i++) cnt++; 
}

int main(){
    pthread_t tid[4];
    for(int i=0; i<4; i++) pthread_create(&tid[i], NULL, run, NULL);
    for(int i=0; i<4; i++) pthread_join(tid[i], NULL);
    
    printf("%d\n", cnt);
    return 0;
}
