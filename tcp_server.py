import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 4000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("TCP Server running...")

while True:
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        message = data.decode()
        print("Received:", message)

        upper_message = message.upper()
        conn.send(upper_message.encode())
        print("Sent:", upper_message)

    conn.close()