
import socket
import threading

class Publisher:
    def __init__(self,topic_name,host=socket.gethostname(),port=5001):
        host=host   # host = 127.0.0.1
        port= port
        self.topic = topic_name  

        self.publisher_client = socket.socket()  # instantiate socket client
        self.publisher_client.connect((host, port)) # connect to server
        self.publisher_client.send( ("publisher:" + str(self.topic)).encode()  )  # inform server that this is a publisher

    def publish(self,msg):       
        if len(msg) != 0:   # checks if input message is not zero 
            msg= str(self.topic) + ":" + str( msg ) # make message in form  of " topic_name: topic msg "
            self.publisher_client.send(msg.encode())  # send message to server

    def close_connection(self):
        self.publisher_client.close() 
        print("connection with server closed")

if __name__== "__main__":
    j=Publisher(topic_name="test")
    j.publish("hi I am message")
    j.publish("avara ka dabra")
    #j.close_connection()

