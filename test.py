from socket import *

udp = socket(AF_INET, SOCK_DGRAM)
udp.bind(("", 7777))
while True:
    print("go on")
    data = udp.recvfrom(1024)
    print(data)
    udp.sendto(b"baka", ("192.168.248.1", 8080))