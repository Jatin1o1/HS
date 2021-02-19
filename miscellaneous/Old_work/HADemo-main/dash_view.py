import webview
import paho.mqtt.client as mqtt
#from speak_light import say


#say("lights have been turned off ")
host = "127.0.0.1"
#html =  "/home/jatin/Downloads/HA/index.html"
html = "./IoT/HA/Dashboard/index.html"

client = mqtt.Client("P1")  # create new instance
client.connect(host)

# function to  publish at mqtt topic Mqtt_publish(topic,message)
def Mqtt_publish(topic,message):   # function to  publish at mqtt topic Mqtt_publish(topic,message)
    client.connect(host)
    client.publish(topic, message)
    client.disconnect()


class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def lock(self, params):
        print(str(params))
        Mqtt_publish("switch", params)        # function to  publish at mqtt topic Mqtt_publish(topic,message)

        
        if params is "0":
            print("Unlocked ")
        if params is "1":
            #say("lights have been turned on")
            print("Locked")

    def fan(self, params):
        print(str(params))
        Mqtt_publish("switch", params)         # function to  publish at mqtt topic Mqtt_publish(topic,message)

    def switch2(self, params):
        print(str(params)) 
        Mqtt_publish("switch", params)          # function to  publish at mqtt topic Mqtt_publish(topic,message)
    

    def switch3(self, params):
        print(str(params)) 
        Mqtt_publish("switch", params)          # function to  publish at mqtt topic Mqtt_publish(topic,message)
    
    def switch4(self, params):
        print(str(params))
        Mqtt_publish("switch", params)              # function to  publish at mqtt topic Mqtt_publish(topic,message)

    def switch5(self, params):
        print(str(params))
        Mqtt_publish("switch", params)          # function to  publish at mqtt topic Mqtt_publish(topic,message)

    def switch6(self, params):
        print(str(params))
        Mqtt_publish("switch", params)          # function to  publish at mqtt topic Mqtt_publish(topic,message)

    def switch7(self, params):
        print(str(params))
        Mqtt_publish("switch", params)          # function to  publish at mqtt topic Mqtt_publish(topic,message)

    def switch8(self, params):
        print(str(params))
        Mqtt_publish("switch", params)
        #client.connect(host)
        #client.publish("switch", params)
        #client.disconnect()

    def switch9(self, params):
        print(str(params))
        Mqtt_publish("switch", params)      # calling function to  publish at mqtt topic Mqtt_publish(topic,message)

api = Api()
window = webview.create_window(
    'API example', html, fullscreen=True, js_api=api)
webview.start(debug=True)
# mosquitto_pub -t "switch" -m "7:0"
