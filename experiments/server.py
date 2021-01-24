#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket               # Import socket module
import threading
import time

max_byte_to_receive=1024 

def on_new_client(clientsocket,addr):
    print  ('Got connection from', addr )
    intro_msg = clientsocket.recv(max_byte_to_receive)
    details= intro_msg.decode().split(":")   # details=["publisher", "test"]  # test is topic here
    print("details are ", details)
    if details[0] == "publisher":  # connected client is publisher 
        # publisher client
        print("it is a publisher")
        while True:
            msg = clientsocket.recv(max_byte_to_receive).decode().split(":")  # msg=[topicname, topic_msg]
            
            if len(msg[1]) !=0 : # topic message 
                print("msg")

    if details[0] == "subscriber":   #  connected client is subscriber
        print("it is a subscriber")
        # subscriber client here
        while True:
            msg="hi client your address is " + str(addr)
            time.sleep(1)
            print(msg)
            clientsocket.sendall(msg.encode())
            msg=''
            #msg = clientsocket.recv(max_byte_to_receive)
            if len(msg) !=0 :
                #do some checks and if msg == someWeirdSignal: break:
                print (addr, ' >> ', msg)    
        
    clientsocket.close()

def socket_server(port = 5005, max_clients=1000, max_byte_to_receive=1024 ):

    server = socket.socket()     # Create a socket object
    host = socket.gethostname()  # Get local machine name

    server.bind((host, port))    # Bind to the port 
    server.listen(max_clients)    # starts listening to the incoming client connection

    print ( 'Server started!')
    print ('Waiting for clients...' )


    while True:
        
        client, addr = server.accept()     # Establish connection with client.
        t=threading.Thread(target=on_new_client, args=(client,addr,) )
        t.start()

    server.close()


if __name__== "__main__":
    socket_server()   # starting socket server
 