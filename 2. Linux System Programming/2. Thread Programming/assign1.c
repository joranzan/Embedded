#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void* run1(){
    char carr[3] = {'A','B','C'};
    while(1){

		for(int i=0;i<3;i++){
			
			printf("[DD1] %c\n",carr[i]); 
			usleep(300*1000);
		}	

	}
}

void* run2(){

	while(1){
		for(int i=1;i<=5;i++){
			printf("[DD2] %d\n",i);
			usleep(200*1000);
		}
	}
}

void* run3(){
	while(1){
		for(char c='A';c<='Z';c++){
			printf("[DD3] %c\n", c);
			usleep(300*1000);

		}

	}

}

int main(){
    pthread_t dd1;
	pthread_t dd2;
	pthread_t dd3;
	
    pthread_create(&dd1, NULL, run1, NULL);
	pthread_create(&dd2, NULL, run2, NULL);
	pthread_create(&dd3, NULL, run3, NULL);

	pthread_join(dd1, NULL);
	pthread_join(dd2, NULL);
    pthread_join(dd3, NULL);

    return 0;
}
