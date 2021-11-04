import socket
import sys
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ipNum = sys.argv[1]
    portNum = sys.argv[2]
    bufferSize = 96
    sendingCounter = 1
    flag = True
    with open(sys.argv[3], "rb") as in_file:
        while True:
            if flag:
                piece = in_file.read(bufferSize)
                if piece == "":
                    break  # end of file
                s.sendto((str(sendingCounter) + "." + piece).encode(), (ipNum, portNum))
            s.settimeout(5)
            try:
                data, address = s.recvfrom(100)
            except socket.timeout:
                flag = False
                continue
            if data.decode("utf-8") != piece:
                flag = False
                continue
            flag = True
            sendingCounter = sendingCounter + 1
    s.close()
if __name__ == '__main__':
     main()