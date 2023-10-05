#include<stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>


int main(){
	
   int fd = open("./num.txt", O_RDONLY, 0);

   if(fd<0){
	   printf("[%s :: %d] FILE OPEN ERROR\n" ,__FILE__, __LINE__);
	   exit(1);
   }

	char buf[10]="";
	read(fd, buf, 10);
	int num = atoi(buf);
	printf("%d\n", num+10);

   close(fd);


	return 0;
}


