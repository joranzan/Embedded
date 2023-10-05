#include<stdio.h>
#include<string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
int main(){
   
	
	
	  int fd = open("./test.txt", O_RDONLY, 0);



      if(fd<0){
          printf("[%s :: %d] FILE OPEN ERROR\n" ,__FILE__, __LINE__)    ;
          exit(1);
      }
		

	  while(1){
       char buf[11]="";
       read(fd, buf, 10);
       printf("===============\n");
		printf("%s\n", buf);

       printf("===============\n");
		printf("%lu\n", strlen(buf));

		if(strlen(buf)<10){
			break;
		}

       

	  }
      close(fd);


       return 0;
   }
