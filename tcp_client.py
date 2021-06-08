#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3
import cv2
import socket
import pickle
import struct

#TCP Socket creation 
tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_port = 2323
server_ip = input("Enter Server IP:")

#Establish Connection
tcp_client_sock.connect((server_ip,server_port))
print(f"Conneted to {server_ip}")
data = b""
payload = struct.calcsize("Q")

while True:
    while len(data) < payload:
        recv_packet = tcp_client_sock.recv(1024)
        if not recv_packet: break
        data += recv_packet
    packed_data = data[:payload]
    data = data[payload:]
    packet_size =  struct.unpack("Q",packed_data)[0]
    
    while len(data) < packet_size:
        data+= tcp_client_sock.recv(1024)
    photo_data = data[:packet_size]
    data = data[packet_size:]
    
    #Deserialise Data
    photo = pickle.loads(photo_data)
    cv2.imshow("Client Side Streaming...", photo)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
tcp_client_sock.close()

