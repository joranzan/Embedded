#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

int main(){
    	int fd = open("./test.txt", O_RDWR | O_TRUNC);
    	if (fd < 0) {
            printf("[%s :: %d] FILE OPEN ERROR\n", __FILE__, __LINE__);
            exit(1);
    	}
	
	char buf[10] = "[NEW]\n";
	write(fd, buf, strlen(buf));
	
	close(fd);

	return 0;
}
