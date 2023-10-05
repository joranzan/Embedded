//lseek() 이용한 샘플 코드
//lseek(fd, offset, whence) : 기준점에서 offset 만큼 떨어진 곳으로 파일 offset을 옮기는 시스템콜

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(){
	int fd = open("./test.txt", O_RDONLY, 0);
	if (fd < 0) {
		printf("[%s :: %d] FILE OPEN ERROR\n", __FILE__, __LINE__);
		exit(1);
	}	
	
	char buf[10] = {0};
	int n = lseek(fd, -7, SEEK_END); //맨뒤에서 -7 이동
	printf("%d\n", n);
	read(fd, buf, 6);
	printf("%s\n", buf);

	memset(buf, 0, 10);
	n = lseek(fd, 0, SEEK_SET); //맨 앞에서 0칸 이동
	printf("%d\n" , n);
	read(fd, buf, 10);
	printf("%s\n", buf);

	memset(buf, 0, 10);
	n = lseek(fd, 5, SEEK_CUR); //현재 위치에서 5칸 뒤로 이동
	printf("%d\n", n);
	read(fd, buf, 6);
	printf("%s\n", buf);

	close(fd);

	return 0;
}
