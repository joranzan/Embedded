#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>


void *gogo() {


	char* week[7] ={"SUN", "MON", "TUE","WED","THU", "FRI","SAT"};

    while(1) {
        
		time_t t = time(0);
		struct tm *tmm = localtime(&t);
 
 		printf("%d/", (tmm->tm_year)+1900);	 
 		printf("%d/", (tmm->tm_mon+1));
 		printf("%d ", tmm->tm_mday);
 		printf("%s\n", week[tmm->tm_wday]);
 		printf("%d : ", tmm->tm_hour);
 		printf("%d : ", tmm->tm_min);
 		printf("%d\n", tmm->tm_sec);
		sleep(1);
    }
}

int main()
{
    pthread_t t;

    pthread_create(&t, NULL, gogo, NULL);

    pthread_join(t, NULL);

    return 0;
}
