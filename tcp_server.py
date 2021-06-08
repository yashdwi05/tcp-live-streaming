#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/python3
import socket
import cv2
import pickle
import struct

#TCP Socket Creation
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcp_sock.bind(("0.0.0.0", 2323))

#Listening To Connections
tcp_sock.listen()
print("Accepting Connections...")

while True:
    s, addr = tcp_sock.accept()
    print(f"Connected to {addr}!!!")
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, photo = cap.read()
        
        #Serialise/flattening Data
        data = pickle.dumps(photo)
        
        #Bytes Conversion
        packet = struct.pack("Q", len(data))+data 
        s.sendall(packet)
        cv2.imshow("Server Side Streaming...",photo)
        if cv2.waitKey(10) == 13:
            cv2.destroyAllWindows()
            cap.release()
            break
tcp_sock.close()


# In[ ]:




