import socket
import sys


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ipNum = sys.argv[1]
    portNum = int(sys.argv[2])
    bufferSize = 100
    sendingCounter = 1
    flag = True
    with open(sys.argv[3], "r") as in_file:
        while True:
            if flag:
                piece = in_file.read(bufferSize - 4)
                if piece == "":
                    break  # end of file
            s.sendto((str(sendingCounter) + "." +
                     piece).encode(), (ipNum, portNum))
            s.settimeout(1)
            try:
                data, address = s.recvfrom(bufferSize)
            except socket.timeout:
                flag = False
                continue
            if data != (str(sendingCounter) + "." + piece).encode():
                flag = False
                continue
            flag = True
            sendingCounter = sendingCounter + 1
    s.close()
    in_file.close()


if __name__ == '__main__':
    main()
