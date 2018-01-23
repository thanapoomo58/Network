import socket

while 1:
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5010
    MESSAGE = input("\nfactorial Number: ")

    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.sendto(str(MESSAGE), (UDP_IP, UDP_PORT))

    data, addr = sock.recvfrom(1024)
    print "message:", MESSAGE
    print 'Server response : ' + data
    #print '\n'
    #print "UDP target IP:", UDP_IP
    #print "UDP target port:", UDP_PORT
