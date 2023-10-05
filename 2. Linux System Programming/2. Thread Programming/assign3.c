#include<stdio.h>
#include<pthread.h>

pthread_t thread[4];


void* run(void* arg){
	
	char* carr[10]={
		"ABC","MINMIN","COCO","KFCKFC"
	};

	int id = *(int*)arg;

	printf("%d %s\n",id+1, carr[id]);

}

int main(){

 	int id[4];	
	for(int i=0;i<4;i++){
		id[i]=i;
		pthread_create(&thread[i],NULL,run,&id[i]);

	}

	for(int i=0;i<4;i++){
		pthread_join(thread[i],NULL);
	}
	



	return 0;
}
