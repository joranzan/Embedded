#include <stdio.h>
#include <time.h>
 
int main(){
  time_t t = time(0);
  struct tm *tmm = localtime(&t);
 
  printf("Year : %d\n", tmm->tm_year);	 
  printf("Month : %d\n", tmm->tm_mon);
  printf("Day : %d\n", tmm->tm_mday);
  printf("Day of the week : %d\n", tmm->tm_wday);
  printf("Hour : %d\n", tmm->tm_hour);
  printf("Min : %d\n", tmm->tm_min);
  printf("Sec : %d\n", tmm->tm_sec);
     
  return 0;
}
