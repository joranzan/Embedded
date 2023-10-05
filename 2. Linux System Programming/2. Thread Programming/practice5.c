#include <stdio.h>
#include <pthread.h>

void *run(void *arg){
	int a = *(int*)arg;
	printf("%d", a);
}

int main(){
	pthread_t t[4];
	for (int i = 0; i<4; i++) pthread_create(&t[i], NULL, run, &i);
	for (int i = 0; i<4; i++) pthread_join(t[i], NULL);	
	return 0;
}
