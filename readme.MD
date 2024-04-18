# Chat app
This is simple server-client chat application, which allows to communicate multiple users in the same time.
### Installing
To get this app just cimple copy this link below into your terminal.
```
git clone git@github.com:Alg1mantas/Chat_application.git
```

### Project description
This application is built using the sockets library, enabling communication between a server and multiple clients. Currently, it has been tested primarily on localhost, with plans for future testing across multiple computers. Additionally, I am committed to enhancing the application by incorporating extra features such as end-to-end encryption and login functionality.

### Project Overview
As one of my first and most cherished projects, I am continuously refining its functionality and usability. While some bugs may be present due to its developmental nature, I encourage feedback from users to identify areas for improvement. Your insights and suggestions are invaluable in shaping the evolution of this project.

### Usage 
It's quite simple to use this application. At first you need to configurate app. In existing code both in server.py and client.py enter IP adress and port number. By default server IP: 127.0.0.1, Port: 8080 . If you are OK about default values it's not nessesary to configure it.

![My Image](images/Server_configuration.PNG)

When configuration is done. Just start client.py or server.py After starting client.py you need to provide user name:

![My Image](images/Client_start.PNG)

After providing user name, client will connect to server

client.py:
![My Image](images/Client_connected.PNG)

server.py:
![My Image](images/Server_connected.PNG)

Now you can communicate to each other

![My Image](images/dialogue.png)

If someone will leave chat , other users will get message:

![My Image](images/user_left_session.png)

If you want to exit chat application just type and press enter:

```
chatquit
```
If server side wants to know how many active users is online , type and press enter:

```
chatlist
```
