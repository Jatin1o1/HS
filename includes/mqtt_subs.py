import paho.mqtt.client as mqtt
import threading

class MQ_subs:

    def __init__(self,host="127.0.0.1",port=1883,topic=''):

        self.topic=topic
        self.message=None  # empty variable to store latest message received
        
        self.client = mqtt.Client()  # Create instance of client 

        self.client.on_connect = self.on_connect  # Define callback function for successful connection
        self.client.message_callback_add(self.topic,self.on_message)
        
        self.client.connect(host,port)  # connecting to the broking server
        
        t=threading.Thread(target=self.subscribe)       # make a thread to loop for subscribing
        t.start() # run this thread
        
    def subscribe(self):
        self.client.loop_forever() # Start networking daemon
        
    def on_connect(self,client, userdata, flags, rc):  # The callback for when the client connects to the broker
        client.subscribe(self.topic)  # Subscribe to the topic, receive any messages published on it
        print("subscriing to topic :",self.topic)


    def on_message(self,client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
        self.message=msg.payload.decode()
        #print("Message received-> " + msg.topic + " " + self.message)  # Print a received msg
        

if __name__ == "__main__":
    # creatign 4 instances of the MQ_subs class
    j=MQ_subs(topic="test")
    k=MQ_subs(topic="test1")
    l=MQ_subs(topic="test2")
    m=MQ_subs(topic="test3")
    print("4 instances created, subscribig to the topics 'test', 'test1', 'test2', 'test3'")

