#include <stdio.h>
#include <unistd.h>

int main(){
	setbuf(stdout,NULL);
  
	int i=0;
	while(1){
		printf("%d ", i);
		i++;
		sleep(1);
	}
	return 0;
}
