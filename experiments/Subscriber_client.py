
import socket
import threading

class Subscriber:
    def __init__(self,topic_name,host=socket.gethostname(),port=5000, max_byte_to_receive= 1024):
        host=host   # host = 127.0.0.1
        port= port   

        self.topic = topic_name
        self.message=None
        self.max_byte_to_receive= max_byte_to_receive  # max bytes of data to receive

        self.subscriber_client = socket.socket()  # instantiate socket client
        self.subscriber_client.connect((host, port))  # connect to server
        self.subscriber_client.send("subscriber:" + str(self.topic) )  # inform server that this is a subscriber

    def subscribe(self):
        t=threading.Thread(target= self.receive) # running recieving function in thread to receive data from server
        t.start()       # starting thread
        

    def receive(self):  # function to receive data form server
        while True:
            msg = self.subscriber_client.recv(self.max_byte_to_receive)     # this line does magic :p
            # add script to verify the topic names
            if len(msg) != 0:
                self.message=msg
                #print(self.message)

    def close_connection(self):
        self.subscriber_client.close()


if __name__== "__main__":
    j=Subscriber(topic_name="test")
    j.subscribe()
    while True:
        print(j.message)
