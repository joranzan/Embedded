#include <stdio.h>
#include <pthread.h>

pthread_mutex_t mlock;
int cnt=0;
void *run(){
	pthread_mutex_lock(&mlock);  //잠그기

	for(int i=0; i<10000; i++) cnt++;

	pthread_mutex_unlock(&mlock); //풀기
}

int main(){
	pthread_mutex_init(&mlock, NULL);
	
	pthread_t tid[4];
	for(int i=0; i<4; i++) pthread_create(&tid[i], NULL, run, NULL);
	for(int i=0; i<4; i++) pthread_join(tid[i], NULL);
	
	printf("%d\n", cnt);
	
	pthread_mutex_destroy(&mlock);

    	return 0;
}
