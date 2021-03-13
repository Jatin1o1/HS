
import paho.mqtt.client as mqtt

host = "127.0.0.1"


client = mqtt.Client("P1")  # create new instance
client.connect(host)

# function to  publish at mqtt topic Mqtt_publish(topic,message)
def Mqtt_publish(topic,message):   # function to  publish at mqtt topic Mqtt_publish(topic,message)
    client.connect(host)
    client.publish(topic, message)
    client.disconnect()


if __name__ == "__main__":
    Mqtt_publish("test", "Hi it is a message")  # topic name is test, messge is "hi it is a message"
