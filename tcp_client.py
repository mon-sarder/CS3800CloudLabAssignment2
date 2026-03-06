import socket

HOST = '10.10.0.101'  # Juliet's IP
PORT = 4000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to TCP server. Type 'quit' to exit.")

while True:
    message = input("Enter message: ")

    if message.lower() == "quit":
        break

    client.send(message.encode())
    data = client.recv(1024)

    print("Server replied:", data.decode())

client.close()