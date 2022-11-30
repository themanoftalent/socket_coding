
#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include "ctype.h" // for isdigit()
#include "sys/socket.h"
#include "arpa/inet.h"
#include "unistd.h"


int main() {
    int socket_desc, client_sock, c, read_size;
    struct sockaddr_in server, client;
    char client_message[2000];

    //burada bir soket oluşturuyoruz
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc == -1) {
        printf("Soket oluşturulamadı");
    }
    puts("soket oluşturuldu");

    // socket yapisi hazirlaniyoruz
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8888);

    // soket baglanıyor 
    if (bind(socket_desc, (struct sockaddr *) &server, sizeof(server)) < 0) {
        //print the error message
        perror("Baglanti hatasi");
        return 1;
    }
    puts("Baglanti basarili");

    // dinleme yapiyoruz
    listen(socket_desc, 3);

    // gelen baglantilari kabul ediyoruz
    puts("Baglanti bekleniyor...");
    c = sizeof(struct sockaddr_in);

    //Client baglantisi kabul ediliyor
    client_sock = accept(socket_desc, (struct sockaddr *) &client, (socklen_t *) &c);
    if (client_sock < 0) {
        perror("Baglanti kabul edilemedi");
        return 1;
    }
    puts("Baglanti kabul edildi");

    //Client mesajini aliyoruz
    while ((read_size = recv(client_sock, client_message, 2000, 0)) > 0) {
        //Send the message back to client
        write(client_sock, client_message, strlen(client_message));
    }

    if (read_size == 0) {
        puts("Client baglantisi kesildi");
        fflush(stdout);
    } else if (read_size == -1) {
        perror("Mesaj alinamadi");
    }

    return 0;
}

