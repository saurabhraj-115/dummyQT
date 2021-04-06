import socket
import socketserver

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3232        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    # s.serve_forever()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        conn.send(b'Welcome\r\n')
        while True:
            data = conn.recv(1024)
            if data:
                print(data)

            else:
                continue
