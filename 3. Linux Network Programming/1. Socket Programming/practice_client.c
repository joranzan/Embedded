//echo_client

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>       
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

const char *IP = "127.0.0.1";
const char *PORT = "12345";

int sock;
void interrupt(int arg){
	printf("\nYou typped Ctrl + C\n");
	printf("Bye\n");

	close(sock);
	exit(1);
}

int main(){
	signal(SIGINT, interrupt);

	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock == -1){
		printf("ERROR :: 1_Socket Create Error\n");
		exit(1);
	}
	//printf("Socket Create!\n");

	struct sockaddr_in addr = {0};
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr(IP);
	addr.sin_port = htons(atoi(PORT));
	
	socklen_t addr_len = sizeof(addr);

	if (connect(sock, (struct sockaddr *)&addr, addr_len) == -1){
		printf("ERROR :: 2_Connect Error\n");
		exit(1);
	}
	//printf("Connect Success!\n");
		
	char buf[100];
	while (1){
		memset(buf, 0, 100);
		scanf("%s", buf);
		if (!strcmp(buf, "exit")){
			write(sock, buf, strlen(buf));
			break;
		}
		write(sock, buf, strlen(buf));

		memset(buf, 0, 100);
		int len = read(sock, buf, 99);
		if (len == 0){
			printf("INFO :: Server Disconnected\n");
			break;
		}
		printf("%s\n", buf);
	}

	close(sock);
	//printf("Logout\n");
	return 0;
}
