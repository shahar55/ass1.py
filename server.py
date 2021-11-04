import socket
import sys

MY_PORT = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', MY_PORT))
packetCounter = 0
while True:
    data, addr = s.recvfrom(100)
    text = str(data.decode())
    numPacket, text = text.split('.', 1)
    if int(numPacket) == packetCounter + 1:
        print(text, addr)
        packetCounter = packetCounter + 1
    s.sendto(data, addr)
