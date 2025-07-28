#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string>
#include <cstring>
#include <iostream>

class PowerSocketClient {
private:
    int sock;
    struct sockaddr_in serv_addr;

public:
    PowerSocketClient(const std::string &host, int port) {
        sock = socket(AF_INET, SOCK_STREAM, 0);
        serv_addr.sin_family = AF_INET;
        serv_addr.sin_port = htons(port);
        inet_pton(AF_INET, host.c_str(), &serv_addr.sin_addr);
        connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    }

    float predict(float voltage, float current) {
        char buffer[1024] = {0};
        std::string msg = std::to_string(voltage) + "," + std::to_string(current);
        send(sock, msg.c_str(), msg.length(), 0);
        read(sock, buffer, 1024);
        return std::stof(buffer);
    }

    ~PowerSocketClient() {
        close(sock);
    }
};

