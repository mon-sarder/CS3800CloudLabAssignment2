import socket

HOST = '0.0.0.0'
PORT = 4001

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("UDP Server running...")

while True:
    data, addr = server.recvfrom(1024)
    message = data.decode()

    print("Received:", message)

    upper_message = message.upper()
    server.sendto(upper_message.encode(), addr)

    print("Sent:", upper_message)