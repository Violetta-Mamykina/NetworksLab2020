import socket
import threading


class ThreadReceive(threading.Thread):
    def __init__(self, server_socket):
        threading.Thread.__init__(self)
        self.ssocket = server_socket

    def run(self):
        while True:
            data = self.ssocket.recv(1024).decode('UTF-8')
            print(data)
            if data == b'':
                break


SERVER = "127.0.0.1"
PORT = 5001
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
login = input("Enter your login: ")
client.send(bytes(login, 'UTF-8'))
while True:
    thread_receive = ThreadReceive(client)
    thread_receive.start()
    out_data = input()
    length = len(out_data)
    client.send(bytes(str(length), 'UTF-8'))
    client.send(bytes(out_data, 'UTF-8'))
#client.close()
