#include<stdio.h>
#include<pthread.h>

char vect[4][21] =
{
    "ABCDEFGHIJKLMNOPQRST",
    "HIFAKERHIFAKERHIFAKE",
    "BBQBBQBBQBBQBBQBBQBB",
    "MACMACMACMACMACMACMA",
};

void *run(void* arg){

	int row = *(int*)arg;
	for(int i=0;i<20;i++){
		vect[row][i] = vect[row][i] + 3;
	}

}

int main(){
	pthread_t tid[4];
	int id[4];

	for(int i=0;i<4;i++){
		id[i] = i;
		pthread_create(&tid[i], NULL, run, &id[i]);
	
	}

	for(int i=0;i<4;i++) pthread_join(tid[i],NULL);

	for(int i=0;i<4;i++){
		printf("%s\n",vect[i]);
	
	}
	return 0;
}
