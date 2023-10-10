#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <pthread.h>

int sock;
pthread_t thRead, thWrite;

void interrupt(int arg) {
    printf("\nYou typped Ctrl + C\n");
    printf("Bye\n");

    close(sock);
    exit(1);
}

void removeEnterChar(char* buf) {
    int len = strlen(buf);
    for (int i = len - 1; i >= 0; i--) {
        if (buf[i] == '\n') {
            buf[i] = '\0';
            break;
        }
    }
}

void* readFromServer() {
    char buf[100];
    while (1) {
        memset(buf, 0, 100);
        int len = read(sock, buf, 99);
        removeEnterChar(buf);

        if (len == 0) {
            printf("INFO :: Server Disconnected\n");
            break;
        }

        int num = atoi(buf);
        char tmp[100];
        sprintf(tmp, "%d", num);

        printf("SERVER : ");
        if (strcmp(buf, tmp) == 0) {
            printf("%d\n", num * 2);
        }
        else {
            printf("%s\n", buf);
        }
    }
}

void* writeToServer() {
    char buf[100];
    while (1) {
        memset(buf, 0, 100);
        scanf("%s", buf);
        if (!strcmp(buf, "exit")) {
            write(sock, buf, strlen(buf));
            pthread_cancel(thRead);
            break;
        }
        write(sock, buf, strlen(buf));
    }
}

int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("ERROR :: Input IP addr, Port Number\n");
        exit(1);
    }

    signal(SIGINT, interrupt);

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        printf("ERROR :: 1_Socket Create Error\n");
        exit(1);
    }
    //printf("Socket Create!\n");

    struct sockaddr_in addr = { 0 };
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(argv[1]);
    addr.sin_port = htons(atoi(argv[2]));

    socklen_t addr_len = sizeof(addr);

    if (connect(sock, (struct sockaddr*)&addr, addr_len) == -1) {
        printf("ERROR :: 2_Connect Error\n");
        exit(1);
    }
    //printf("Connect Success!\n");

    pthread_create(&thRead, NULL, readFromServer, NULL);
    pthread_create(&thWrite, NULL, writeToServer, NULL);

    pthread_join(thRead, NULL);
    pthread_join(thWrite, NULL);

    close(sock);
    //printf("Logout\n");
    return 0;
}
