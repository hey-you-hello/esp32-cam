import camera
import io
import time
import socket

import sys


camera.deinit()
HOST = '0.0.0.0'  
PORT = 8080       
def mainf():
    if True :
        server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        while True:
            conn, addr = server.accept()
            if True:
                print(f"Connected by {addr}")
                computer=addr
                data = conn.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")
                    
                    conn.sendall(b'hello client')
                    break

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if camera.init():
        camera.framesize(10)
        #800*600巷素
        camera.quality(60)  
        print("Camera initialized.")
       
    else:
        print("Camera failed to initialize.")
    print('start dendding img.....')

    while True:
        try:
            s.sendto(camera.capture(),(computer[0],8080))
        except KeyboardInterrupt:
            camera.deinit()
            
            print('end process!')
            sys.exit()
        

mainf()
