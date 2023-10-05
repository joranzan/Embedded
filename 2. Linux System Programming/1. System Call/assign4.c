#include<stdio.h>
#include<string.h>
#include <sys/types.h>

#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
 int main(){
    int fd = open("./cal.txt", O_RDONLY, 0644);

     if(fd<0){
         printf("[%s :: %d] FILE OPEN ERROR\n" ,__FILE__, __LINE__);
         exit(1);
     }
 
      char buf[10]="";
      read(fd, buf, 10);


	  int num = atoi(buf);
	  printf("%d\n", num);
      
	  num *= 2;

	  sprintf(buf, "%d", num);
	  
   	 int fd2 = open("./cal.txt", O_WRONLY | O_TRUNC, 0644);
	 write(fd2, buf, strlen(buf));
 
      close(fd);
 	close(fd2);
 
      return 0;
  }

