#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>       
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>

int sock;

void interrupt(int arg){
	printf("\nYou typed Ctrl + C\n");
	printf("BYE\n");
	
	close(sock);
	exit(1);
}

int main(int argc, char* argv[]){

	if(argc!=3){
		printf("ERROR Input IP addr, Port num\n");
		exit(1);
	}

	signal(SIGINT, interrupt);

	const char *IP = argv[1];
	const char *PORT = argv[2];

	
	//socket create
	
	sock = socket(AF_INET, SOCK_STREAM, 0);
	if (sock == 0){
		printf("ERROR :: 1_Socket Create Error\n");
		exit(1);
	}
	printf("Socket Create!\n");
	
	//Socket Structure
	struct sockaddr_in addr = {0};
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr(IP);
	addr.sin_port = htons(atoi(PORT));
	
	socklen_t addr_len = sizeof(addr);

	
	//connect
	if(connect(sock, (struct sockaddr *)&addr, addr_len) == -1){
		printf("ERROR :: 2_Connect Error\n");
		exit(1);
	}
	printf("Server Connected Successfully\n");
	
	
	//Read/Write

	char buf[100];
	
	while(1){
		memset(buf, 0, 100);
		scanf("%s", buf);

		if(!(strcmp(buf, "exit"))){

				write(sock, buf, strlen(buf));
				break;
		}

		write(sock, buf, strlen(buf));

		memset(buf, 0, 100);
		
		int len = read(sock, buf, 99);
		
		if(len == 0){
			printf("INFO :: Server Disconnected\n");
			break;
		}

		printf("%s\n", buf);
		

	}
	
	close(sock);
	printf("You typed exit.\nLog Out\n");

	return 0;



	return 0;

}
