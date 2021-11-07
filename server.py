import socket
import sys


def main():
    if len(sys.argv) != 2:
        print("Number of arguments isn't correct.")
        return
    if int(sys.argv[1]) > 65535 or int(sys.argv[1]) < 1:
        print("Port number isn't valid.")
        return
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
        if text == "end":
            clientCounterDict[addr] = 0
        else:
            numPacket, text = text.split('.', 1)
            if int(numPacket) == clientCounterDict[addr] + 1:
                print(text, end='')
                clientCounterDict[addr] = clientCounterDict[addr] + 1
        s.sendto(data, addr)


if __name__ == '__main__':
    main()
