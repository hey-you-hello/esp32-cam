import socket
import os
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2
import keyboard
ev=keyboard.KeyboardEvent
ON=True.to_bytes()
OFF=False.to_bytes()
output_file = "found_ip.txt"
led_type={'KeyboardEvent(w down)':ON,'KeyboardEvent(s down)':OFF}
current_type=OFF
def o(e):
    global current_type
    if str(e) not in led_type:
         print(f'沒有{e}')
         return 0
    current_type=led_type[str(e)]

for n in range(256):
    ip = f'192.168.4.{n}'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f'Trying to connect to {ip}...')
        s.settimeout(0.2)
        s.connect((ip, 8080))
        s.sendall(b'hi am computer')
        print(f'Successfully sent to {ip}')
            
           
        with open(output_file, 'w') as f:  
                f.write(ip + '\n')

        print(f'IP address {ip} saved to {output_file}')
        break  
    except Exception:
        print(f'{ip} no response')
    finally:
        s.close()


class CameraApp:
    def __init__(self, window, window_title, ip):
        self.window = window
        self.window.title(window_title)
        self.ip = ip
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', 8080))

        self.label = tk.Label(window)
        self.label.pack()
        self.canvas = tk.Canvas(window, width = 240, height = 240)
        self.canvas.pack()
        
        self.delay = 5
        self.update()

    def update(self):
        
            data, address = self.socket.recvfrom(65535)
            
            print(f"Received data from {address}, length: {len(data)}")
            keyboard.on_press(o)
            self.socket.sendto(current_type,address)

            
            nparr = np.frombuffer(data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is not None:
                
                img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                self.photo = ImageTk.PhotoImage(image=img_pil)
                self.label.configure(image=self.photo)

            
            self.window.after(self.delay, self.update)


print('開始')
App = CameraApp(tk.Tk(), "攝影機畫面", ip)
App.window.mainloop()
