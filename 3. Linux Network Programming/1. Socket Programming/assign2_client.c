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

int isNumeric(const char *input) {
    for (int i = 0; input[i] != '\0'; i++) {
        if (!(input[i] >= '0' && input[i] <= '9')) {
            // 만약 문자열 중에 숫자가 아닌 다른 문자가 있다면
            return 0;
        }
    }
    return 1;
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
		printf("to Server : ");
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

		if(isNumeric(buf)==1){
		int recieveNum = atoi(buf);
		printf("from Server : %d\n", recieveNum*2);

		}
		else printf("from Server : %s\n", buf);
		

	}
	
	close(sock);
	printf("You typed exit.\nLog Out\n");

	return 0;



	return 0;

}
