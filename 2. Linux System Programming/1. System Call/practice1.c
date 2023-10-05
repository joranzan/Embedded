//시스템콜을 이용한 open/read/close 샘플코드
//main() 를 먼저 작성한뒤, man 페이지를 이용해 헤더 파일을 복사해온다.
//open() / close() / read()
//open() : path, flag, mode
//close() : 파일디스크립터
//read() : 파일디스크립터, 보관할문자열주소, 길이

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	int fd = open("./test.txt", O_RDONLY, 0);
	 //return 값이 음수면 Error!
	if( fd<0 ){
		printf("ERROR\n");
		exit(1); //프로그램이 비정상종료 -> 1
		//프로그램 정상 정료(default : 0) -> exit(0)
	}

	char buf[1000] = {0};
	read(fd, buf, 1000-1);

	printf("%s\n", buf);
	close(fd); //open과 close는 세트
	return 0;
}
