//chat_server.c

#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <pthread.h>

#define MAX_CLIENT_CNT 500

char PORT[6];
int server_sock; 
int client_sock[MAX_CLIENT_CNT] = {0};
struct sockaddr_in client_addr[MAX_CLIENT_CNT] = {0};

pthread_t tid[MAX_CLIENT_CNT];
int exitFlag[MAX_CLIENT_CNT];

pthread_mutex_t mlock;

void interrupt(int arg){
	printf("\nYou typed Ctrl + C\n");
	printf("Bye\n");

	for (int i = 0; i < MAX_CLIENT_CNT; i++){
		if (client_sock[i] != 0){
			pthread_cancel(tid[i]);
			pthread_join(tid[i], 0);
			close(client_sock[i]);
		}
	}
	close(server_sock);
	exit(1);
}

void removeEnterChar(char *buf){
	int len = strlen(buf);
	for (int i = len - 1; i >= 0; i--)	{
		if (buf[i] == '\n') {
			buf[i] = '\0';
			break;
		}
	}
}

int getClientID(){
	for (int i = 0; i < MAX_CLIENT_CNT; i++){
		if (client_sock[i] == 0)
			return i;
	}
	return -1;
}


int isNumeric(const char* input) {
	for (int i = 0; input[i] != '\0'; i++) {
		if (!(input[i] >= '0' && input[i] <= '9')) {
			// 만약 문자열 중에 숫자가 아닌 다른 문자가 있다면
			return 0;
		}
	}
	return 1;
}

void encoding(char* origin, const char* sub, const char* replace) {

	char result[100];
	for (int i = 0; i < strlen(origin); i++) {
		if (strncmp(origin + i, sub, 3) == 0) {
			strcpy(result + i, replace);
			i += 2;
		}
		else {
			result[i] = origin[i];
		}
	}
	result[strlen(origin)] = '\0';
	strcpy(origin, result);

}



void *client_handler(void *arg){
	int id = *(int *)arg;

	char client_IP[100];
 
	strcpy(client_IP, inet_ntoa(client_addr[id].sin_addr));
	printf("INFO :: Connect new Client (ID : %d, IP : %s)\n", id, client_IP);

	char buf[100];
	while (1)	{
		
		memset(buf, 0, 100);
		int len = read(client_sock[id], buf, 99);
		int cmd =0;
		char name[100];
		char mystring[100];
		memset(mystring, 0, 100);

		sscanf(buf, "%s %d %s", name, &cmd, mystring);

		if (len == 0)		{
			printf("INFO :: Disconnect with client.. BYE\n");
			exitFlag[id] = 1;
			break;
		}

		if (!strcmp("exit", buf))		{
			printf("INFO :: Client want close.. BYE\n");
			exitFlag[id] = 1;
			break;
		}

		removeEnterChar(buf);
		pthread_mutex_lock(&mlock);
		
		  if (cmd == 1) {
					
					
			        sprintf(buf, "%s %s", name, mystring);
					if (isNumeric(mystring) == 0) {
						encoding(buf, "ABC", "DEF");
					}
					else {
						int num = atoi(mystring);
						num *= 2;
						sprintf(mystring, "%d", num);
						sprintf(buf, "%s %s", name, mystring );
					}
					
					

			  }
  		else if (cmd == 2) {
	
				  sprintf(buf, "%s %s", name, mystring);
				  if (isNumeric(mystring) == 0) {
					  encoding(buf, "DEF", "ABC");
				  }
				  else {
					  int num = atoi(mystring);
					  num /= 2;
					  sprintf(mystring, "%d", num);
					  sprintf(buf, "%s %s", name, mystring);
				  }
			  }





		for (int i = 0; i < MAX_CLIENT_CNT; i++){
			if (client_sock[i] != 0){

				write(client_sock[i], buf, strlen(buf));
			}
		}
		pthread_mutex_unlock(&mlock);
	}
	close(client_sock[id]);
}


int main(int argc, char* argv[]){
	if( argc<2 ){
		printf("ERROR Input Port Num\n");
		exit(1);
	}
	strcpy(PORT, argv[1]);

	signal(SIGINT, interrupt);
	pthread_mutex_init(&mlock, NULL);

	server_sock = socket(AF_INET, SOCK_STREAM, 0);
	if (server_sock == -1){
		printf("ERROR :: 1_Socket Create Error\n");
		exit(1);
	}	
	printf("Server On..\n");	

	int optval = 1;
	setsockopt(server_sock, SOL_SOCKET, SO_REUSEADDR, (void *)&optval, sizeof(optval));

	struct sockaddr_in server_addr = {0};
	server_addr.sin_family = AF_INET;
	server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
	server_addr.sin_port = htons(atoi(PORT));

	if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1){
		printf("ERROR :: 2_bind Error\n");
		exit(1);
	}
	printf("Bind Success\n");
	
	if (listen(server_sock, 5) == -1){
		printf("ERROR :: 3_listen Error");
		exit(1);
	}
	printf("Wait Client...\n");

	socklen_t client_addr_len = sizeof(struct sockaddr_in);

	int id_table[MAX_CLIENT_CNT];

	while (1){

		int id = getClientID();
		id_table[id] = id;

		if (id == -1){
			printf("WARNING :: Client FULL\n");
			sleep(1);
		}

		memset(&client_addr[id], 0, sizeof(struct sockaddr_in));

		client_sock[id] = accept(server_sock, (struct sockaddr *)&client_addr[id], &client_addr_len);

		if (client_sock[id] == -1){
			printf("ERROR :: 4_accept Error\n");
			break;
		}

		pthread_create(&tid[id], NULL, client_handler, (void *)&id_table[id]);

		for (int i = 0; i < MAX_CLIENT_CNT; i++){
			if (exitFlag[i] == 1){
				exitFlag[i] = 0;
				pthread_join(tid[i], 0);
				client_sock[i] = 0;
			}
		}
	}
 	pthread_mutex_destroy(&mlock);
	close(server_sock);
	return 0;
}
