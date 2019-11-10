#!/usr/bin/python
import socket
import sys

ip = input('Enter IP:')
ip2 = socket.gethostbyname(ip)

print("-" * 60)
print("Wait the scanning")
print("-" * 60)

try:
    for port in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        tcp = s.connect_ex((ip2,port))

        if tcp == 0:

            if port != 80:
                service = socket.getservbyport(port)
                print("[TCP] Port " + str(port) + " Open - - - Service: " + service)

            else:
                 service = socket.getservbyport(port)
                 s.send("GET / HTTP/1.0\r\n\r\n".encode())
                 f = s.recv(1024)
                 if 'Found\\r\\nServer:' in str(f):
                         b = str(f).split()
                         bb = b[b.index('Found\\r\\nServer:') + 1]
                         webserver=bb.split('\\r')[0]

                         print("[TCP] Port " + str(port) + " Open - - - Service: " + service+ "  Web Server: " +webserver)
                 else:
                     print("[TCP] Port " + str(port) + " Open - - - Service: " + service)

        s.close()

    print("-" * 60)

    for port in range (1,40):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp = socket.socket().connect_ex((ip2, port))
        print("[UDP] Port %d:     Open" % (port))

        sock.close()

    print("-" * 60)

    print('Finished')

except socket.error:
    print("Could not connect")
    sys.exit()
