import socket
import sys

MY_PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', MY_PORT))
packetCounter = 0
while True:
    data, addr = s.recvfrom(100)
    text = str(data)
    numPacket, text = text.split('.', 1)
    if numPacket == packetCounter + 1:
        print(text)
        packetCounter = packetCounter + 1
    s.sendto(data, addr)
