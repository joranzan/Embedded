//lseek() 과 write() 를 이용한 글자 지우기
//0x7F 를 이용해서 글자를 지울 수 있다.
//ASCII CODE 로 DEL 에 해당한다.

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(){
	int fd = open("./test.txt", O_RDWR);
    if (fd < 0) {
		printf("[%s :: %d] FILE OPEN ERROR\n", __FILE__, __LINE__);
		exit(1);
    }	
	
	lseek(fd, 1, SEEK_SET);	    //처음 위치에서 1칸 이동 -> 1의 위치에 쓴다.
	char buf[10] = {0x7F};      //1 대신, DEL이 적히고, DEL 앞에 있는 0이 사라진다.
	write(fd, buf, strlen(buf)); //0"DEL"23456789ABCDEFINISH
  
	close(fd);

	return 0;
}
