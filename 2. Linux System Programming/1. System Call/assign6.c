 #include<stdio.h>
#include<string.h> 
#include <sys/types.h>
 #include <sys/stat.h>
 #include <fcntl.h>
 #include <unistd.h>
 #include <stdlib.h>
  int main(){
     int fd = open("./num.txt", O_RDONLY, 0);

      if(fd<0){
          printf("[%s :: %d] FILE OPEN ERROR\n" ,__FILE__, __LINE__)    ;
          exit(1);
      }

       char buf[27]="";
 		int n = lseek(fd, 0, SEEK_SET);
		read(fd, buf,5);
		printf("%s\n", buf);

		memset(buf,0,27);
		n = lseek(fd, -6, SEEK_END);
		read(fd, buf, 5);
		printf("%s\n", buf);
		
		
		memset(buf,0,27);
		n = lseek(fd, 0, SEEK_SET);
		while(n<27){
		//	printf("%d\n", n);
			char temp[4]="";
			read(fd, temp, 3);
			if(strcmp(temp, "GHI")==0){
				n = lseek(fd, 5, SEEK_CUR);
				char ans[4]="";
				read(fd, ans, 3);
				printf("%s\n", ans);
				break;
			}
			else{
				n= lseek(fd, -2, SEEK_CUR);
	
			}
		}
 	   	

      close(fd);


       return 0;
   }
