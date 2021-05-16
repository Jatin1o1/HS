from threading import Timer
import paho.mqtt.client as mqtt


class Mqtt_Repeated_publisher(object):

    def __init__(self, topic, message, interval,start= True,host="127.0.0.1", port=1883 ):

        self.host=host    # host of mqtt broker
        self.port=port    # port of mqtt broker

        self.topic = topic      # topic on which data is to be sent
        self.message = message   # message to be sent 
        self.interval = interval # time delay between messages
        
        self._timer = None
        self.is_running = False
        
        self.mqtt_client = mqtt.Client("Mqtt_Repeated_publisher")  # create new publisher instance for publishing to mqtt broker

        if start == True:
            self.start()        

    def Mqtt_publish(self):
        self.mqtt_client.connect(self.host, self.port)
        self.mqtt_client.publish(self.topic, self.message)
        self.mqtt_client.disconnect()
    
    def _run(self):
        self.is_running = False
        self.start()
        self.Mqtt_publish()

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

if __name__ == "__main__":

    obj1 = Mqtt_Repeated_publisher("test", "hi", 1)   # automatically start publishing upon construction call
    obj2 = Mqtt_Repeated_publisher("test1", "hi1", 1, False )  # automatically doesnt starts publishing
    
