import socket
import sys


def main():
    MY_PORT = int(sys.argv[1])
    BUFFER_SIZE = 100

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', MY_PORT))
    clientCounterDict = {}
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        if not addr in clientCounterDict.keys():
            clientCounterDict[addr] = 0
        text = str(data.decode())
        numPacket, text = text.split('.', 1)
        if int(numPacket) == clientCounterDict[addr] + 1:
            print(text, end='')
            clientCounterDict[addr] = clientCounterDict[addr] + 1
        s.sendto(data, addr)


if __name__ == '__main__':
    main()
