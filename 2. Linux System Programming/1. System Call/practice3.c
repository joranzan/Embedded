//write() 시스템콜 사용하는 샘플 코드
//test.txt 파일이 없으면 생성한다.

//O_CREAT : 파일 생성
//O_WRONLY : 파일 쓰기 모드로 열기
//write() : 파일 디스크립터, 문자열, 길이

#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int fd = open("./test.txt", O_WRONLY | O_CREAT, 0664);
    if (fd < 0) {
        printf("[%s :: %d] FILE OPEN ERROR\n", __FILE__, __LINE__);
        exit(1);
    }

    char* buf = "Embedded System Programming\n";
    write(fd, buf, strlen(buf));

    close(fd);

    return 0;
}
