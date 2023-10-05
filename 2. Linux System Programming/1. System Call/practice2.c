#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    int fd = open("./test.txt", O_RDONLY, 0);
    if (fd < 0) {
        printf("[%s :: %d] FILE OPEN ERROR\n", __FILE__, __LINE__);
        exit(1);
    }

    char buf[10] = {0};
    ssize_t i = read(fd, buf, 10); //파일을 읽어서 buf의 크기만큼 저장 

    printf("%s %lu\n", buf,i);

    close(fd);
    return 0;
}
