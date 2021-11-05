import socket
import sys


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ipNum = sys.argv[1]
    portNum = int(sys.argv[2])
    bufferSize = 100
    sendingCounter = 1
    packetFlag = True
    endFlag = False
    with open(sys.argv[3], "r") as in_file:
        while True:
            if packetFlag:
                piece = in_file.read(bufferSize - 4)
                if piece == "":
                    message = "end".encode()
                    endFlag = True
                else:
                    message = (str(sendingCounter) + "." + piece).encode()
            s.sendto(message, (ipNum, portNum))
            s.settimeout(1)
            try:
                data, address = s.recvfrom(bufferSize)
            except socket.timeout:
                packetFlag = False
                continue
            if data == message and endFlag:
                break
            if data != message:
                packetFlag = False
                continue
            packetFlag = True
            sendingCounter = sendingCounter + 1
    s.close()
    in_file.close()


if __name__ == '__main__':
    main()
