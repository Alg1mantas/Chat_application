import socket
import threading
import os


HOST = "127.0.0.1"
PORT = 8080
SERVER_NAME = "Server: "

class Server:
    def __init__(self) -> None:
        self.address_list = []
        print(' Server will start on host : ', HOST)
        self.socket = socket.socket()
        self.socket.bind((HOST, PORT))
        print('Waiting for connection')
        self.lock = threading.Lock()
        self.multithreads()


    def multithreads(self) -> None:
        (threading.Thread(target=self.send_message)).start()
        (threading.Thread(target=self.receive_messages)).start()
        (threading.Thread(target=self.port_listener)).start()


    def port_listener(self) -> None:
        while True:
            print("Server is listening for new connection")
            self.socket.listen()
            address, ip = self.socket.accept()
            self.lock.acquire()
            self.address_list.append(address)
            self.lock.release()
            print(ip, " Has connected to the server")


    def send_message(self) -> None:
        while True:
            message = input(str('>> '))
            encoded_message = (SERVER_NAME + message).encode()
            if str(message) == "chatquit":
                print("you pressed quit and choose to close program, Have a nice day! ")
                os._exit(0)
            if str(message) == "chatlist":
                print(f"active connections: ", (len(self.address_list)))
                continue
            for address in self.address_list:
                try:
                    address.send(encoded_message)
                except:
                    print("unknown user left chat")
                    self.user_quit(address=address, username="unknown user")


    def receive_messages(self) -> str:
        while True:
            for address in self.address_list:
                try:
                    address.settimeout(0.01)
                    incoming_message = address.recv(1024).decode()
                    msg_list = incoming_message.split()
                    if msg_list[1] == "quit":
                        print(incoming_message)
                        self.user_quit(address=address, username=msg_list[0])
                        continue
                    print(incoming_message)
                    self.transmit_client_messages(incoming_message=incoming_message, sender_address=address)
                except: Exception


    def user_quit(self, address:object, username:str) -> None:
        self.transmit_client_messages(incoming_message=(username+" Has just left session"), sender_address=address)
        self.lock.acquire()
        self.address_list.remove(address)
        self.lock.release()


    def transmit_client_messages(self, incoming_message:str, sender_address:object)  -> None:
        for address in self.address_list:
            if address == sender_address:  
                continue
            try:
                address.send(incoming_message.encode())
            except:
                print("unknown user left chat ")
                self.user_quit(address=address, username="unknown user")


if __name__=="__main__":
    _ = Server()