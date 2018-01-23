import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5334
BUFFER_SIZE = 3145728
img = open('icon.png','rb')
image = img.read()
img.close()
MESSAGE = (image)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send (str(MESSAGE))
data = s.recv(BUFFER_SIZE)

print "up : ",data



