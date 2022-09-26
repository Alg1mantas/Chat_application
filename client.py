import socket
from threading import Thread
import time
import os

HOST = "127.0.0.1"
PORT = 8080
USERNAME = input("enter your name: ")


class Client:
    def __init__(self) -> None:
        self.address = self.maintain_connection()
        (Thread(target=self.send_message)).start()
        (Thread(target=self.receive_messages)).start()


    def receive_messages(self) -> str:
        while True:
            try:
                incoming_message = self.address.recv(1024)
                incoming_message = incoming_message.decode()
                print(incoming_message)
            except:
                print("connection is lost", end='\r')
                time.sleep(0.3)
                self.address = self.maintain_connection()


    def send_message(self) -> None:
        while True:
            message = input(str('>> '))
            if message == "chatquit":
                self.close_connection()
            message = (USERNAME + " : " + message).encode()
            try:
                self.address.send(message)
            except: Exception


    def close_connection(self) -> None:
        print("you pressed quit and choose to close program, Have a nice day! ")
        message = USERNAME + " quit"
        message = message.encode()
        self.address.send(message)
        self.address.shutdown(socket.SHUT_RDWR)
        os._exit(0)


    def maintain_connection(self) -> object:
        trying_to_connect =  1
        while (trying_to_connect == 1):
            try:
                address = socket.socket()
                address.connect((HOST, PORT))
                print('Connected to chat server')
                trying_to_connect == 0
                return address
            except:
                print("Trying to connect   ", end = '\r')
                time.sleep(0.3)
                print("Trying to connect. ", end = '\r')
                time.sleep(0.3)
                print("Trying to connect.. ", end = '\r')
                time.sleep(0.3)
                print("Trying to connect... ", end = '\r')
                time.sleep(1)


if __name__=="__main__":
    _ = Client()