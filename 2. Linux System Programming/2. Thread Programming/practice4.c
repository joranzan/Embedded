#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

struct Node{
    int y;
    int x;
};

void *abc(void *p){
    struct Node *val1 = (struct Node *)p;
    printf("val1 %d %d\n", val1->x, val1->y);

	struct Node val2 = *(struct Node*)p;
	printf("val2 %d %d \n", val2.x, val2.y);
}

int main(){
    pthread_t t;

    struct Node val = {2, 4};

    pthread_create(&t, NULL, abc, &val);
    pthread_join(t, NULL);

    return 0;
}
