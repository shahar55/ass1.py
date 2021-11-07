import socket
import sys


def main():
    if len(sys.argv) != 4:
        print("Number of arguments isn't correct.")
        return
    if int(sys.argv[2]) > 65535 or int(sys.argv[2]) < 1:
        print("Port number isn't valid.")
        return
    ipNums = sys.argv[1].split('.')
    if len(ipNums) != 4:
        print("IP address isn't valid.")
        return
    for num in ipNums:
        if int(num) > 255 or int(num) < 0:
            print("IP address isn't valid.")
            return
    ipNum = sys.argv[1]
    portNum = int(sys.argv[2])
    bufferSize = 100
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sendingCounter = 1
    packetFlag = True
    endFlag = False
    try:
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
        in_file.close()
    except IOError:
        print("The file does not exist.")
        return
    finally:
        s.close()


if __name__ == '__main__':
    main()
