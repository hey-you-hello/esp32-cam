import camera
import io
import time
import socket
from machine import Pin
import sys
led=Pin(4,Pin.OUT)
led.value(0)
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
        #240x240
        camera.quality(60)  
        print("Camera initialized.")
       
    else:
        print("Camera failed to initialize.")
    print('start dendding img.....')

    while True:
        try:
            s.sendto(camera.capture(),(computer[0],8080))
            data, address=s.recvfrom(65535)
            data=int.from_bytes(data,'big')
            
            led.value(data)
                
        except KeyboardInterrupt:
            camera.deinit()
            
            print('end process!')
            sys.exit()
        

mainf()
