#!/usr/bin/python           # This is server.py file                                                                                                                                                                           

import socket               # Import socket module
import threading
import time

port = 5005

max_byte_to_receive=1024
max_no_of_clients = 1000

def on_new_client(clientsocket,addr):
    print  ('Got connection from', addr )
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

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
            # Reserve a port for your service.



s.bind((host, port))        # Bind to the port
s.listen(max_no_of_clients)                 # Now wait for client connection.

print ( 'Server started!')
print ('Waiting for clients...' )

while True:
   c, addr = s.accept()     # Establish connection with client.
   t=threading.Thread(target=on_new_client, args=(c,addr,) )
   t.start()
   #thread.start_new_thread(on_new_client,(c,addr))
   #Note it's (addr,) not (addr) because second parameter is a tuple
   #Edit: (c,addr)
   #that's how you pass arguments to functions when creating new threads using thread module.
s.close()
