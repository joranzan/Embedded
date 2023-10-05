#include<stdio.h>
#include<pthread.h>

pthread_t thread[37];

void *run(void *arg){

	int num = *(int*)arg;
	printf("%d ",num);
}


int main(){

	int arr[37];
	for(int i=0;i<37;i++){
		arr[i]= i+1;
		pthread_create(&thread[i],NULL, run, &arr[i]);
	}

	for(int i=0;i<37;i++) pthread_join(thread[i], NULL);

	printf("VVCC END\n");



	return 0;
}
