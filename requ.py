import socket

output_file = "found_ip.txt"

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
