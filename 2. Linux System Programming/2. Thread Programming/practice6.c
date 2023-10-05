#include<stdio.h>
#include<pthread.h>
#include <stdlib.h>

int a = 100; //.data
int b;		 //.bss
void* abc(){
    int c = 10; //stack
    printf("=================\n");
    printf(".data  : 0x%p\n", (void*)&a);
    printf(".bss   : 0x%p\n", (void*)&b);
    printf(".stack : 0x%p\n", (void*)&c);
    printf(".heap  : 0x%p\n", (int*)malloc(4));
    return 0;
}


int main(){
    pthread_t t1, t2;
    pthread_create(&t1, NULL, abc, NULL);
    pthread_create(&t2, NULL, abc, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    return 0;
}
