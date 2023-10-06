#include<stdio.h>
#include<pthread.h>

void* run(){
	while(1);
}

int main(){
	
	pthread_t tid[4];

	for(int i=0; i<4; i++) pthread_create(&tid[i],NULL,run,NULL);
	for(int i=0; i<4; i++) pthread_join(tid[i], NULL);

	return 0;
}
