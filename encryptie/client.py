import socket
import threading
import getpass
import sys

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            if ':' in message:
                sender, msg = message.split(':', 1)
                print(f"\n{sender}: {msg.strip()}")
            else:
                print(f"\n{message}")
            print("You: ", end="", flush=True)
        except:
            break

def start_client(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 5555))

    # Use the logged-in user's name
    name = getpass.getuser()
    client.send(name.encode('utf-8'))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = input("You: ")
        if message.startswith('/'):
            # Handle commands starting with /
            if message == '/list':
                client.send('/list'.encode('utf-8'))
            elif message == '/quit':
                client.send('/quit'.encode('utf-8'))
                client.close()
                break
            else:
                print("Unknown command")
        else:
            client.send(message.encode('utf-8'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <server_ip>")
        sys.exit(1)
    server_ip = sys.argv[1]
    start_client(server_ip)