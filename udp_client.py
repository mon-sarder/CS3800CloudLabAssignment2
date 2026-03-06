import socket

HOST = '10.10.0.101'
PORT = 4001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Connected to UDP server. Type 'quit' to exit.")

while True:
    message = input("Enter message: ")

    if message.lower() == "quit":
        break

    client.sendto(message.encode(), (HOST, PORT))
    data, _ = client.recvfrom(1024)

    print("Server replied:", data.decode())

client.close()