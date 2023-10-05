#include<stdio.h>
#include<unistd.h>
#include<pthread.h>
#include<string.h>


pthread_mutex_t mlock;
pthread_t thread[100];
int DAT[100]={0};
int coin =0 ;

void* run(void *arg){
	
	pthread_mutex_lock(&mlock);

	int id = *(int*)arg;

	while(DAT[id]==1){

		coin++;
		usleep(100*1000);

	}

	pthread_mutex_unlock(&mlock);



}


int main(){

	int thread_num = 0;
	int thread_temp[100];
	int del_num = 0;

	pthread_mutex_init(&mlock,NULL);

	while(1){
	
		char query[100];

//		int executed = 0;
//		for(int m=0;m<100;m++){
//			if(DAT[m]==1)	executed++;	

//		}

//		printf("%d threads are exectued\n",executed);
		
		printf("ssafy >> ");
		scanf("%s", query);

		//생성한 코인 출력 
		if(strcmp(query,"show")==0){

			printf("%d\n",coin);


		}
		//채굴기 생성 명령어
		else if(strcmp(query, "add")==0){
			
			thread_temp[thread_num]=thread_num;
			pthread_create(&thread[thread_num], NULL, run, &thread_temp[thread_num]);
			DAT[thread_num] = 1;
			thread_num++;
			if(thread_num==100) thread_num=0;



		}
		//채굴기 제거 명령어
		else if(strcmp(query,"del")==0){
			if(DAT[del_num]==0) continue;
			DAT[del_num] = 0;
			
			pthread_join(thread[del_num],NULL);
			del_num++;
			if(del_num==100) del_num=0;
		}
		else if(strcmp(query,"exit")==0){
			break;
		}
		else{

			printf("Command is unvalid\n");
		}			



	}

	
	pthread_mutex_destroy(&mlock);


	return 0;
}
