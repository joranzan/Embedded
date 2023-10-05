 #include<stdio.h>
 #include<string.h>
 #include <sys/types.h>
 #include <sys/stat.h>
 #include <fcntl.h>
 #include <unistd.h>
 #include <stdlib.h>
  int main(){

	  int c;
	  scanf("%d", &c);

     int fd1 = open("./test.txt", O_RDONLY, 0);

      if(fd1<0){
          printf("[%s :: %d] FILE OPEN ERROR\n" ,__FILE__, __LINE__)    ;
          exit(1);
      }


	  char buf[10][10]={0};
	  
	  for(int i=0;i<9;i++){
		read(fd1,buf[i],9);
	  }

//	for(int i=0;i<10;i++){
//		for(int j=0;j<10;j++){
//			printf("%c", buf[i][j]);
//		}		
//	}	


	close(fd1);

	int fd2 = open("./test.txt",O_WRONLY | O_TRUNC, 0646);
	      
	if(fd2<0){
          printf("[%s :: %d] FILE OPEN ERROR\n" ,__FILE__, __LINE__)    ;
          exit(1);
      }
	

	for(int i=0;i<9;i++){
	//	printf("%c ", buf[i][0]);	
		int num = buf[i][0]-'0';
	//	printf("%d\n", num);
		if(num == c) continue;
		write(fd2, buf[i], 9);
	}


	  close(fd2);

       return 0;
   }

