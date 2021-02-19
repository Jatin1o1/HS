import webview
import paho.mqtt.client as mqtt 
#from speak_light import say


#say("lights have been turned off ")
host="127.0.0.1"
#html =  "/home/jatin/Downloads/HA/index.html" 
#html= "/home/Desktop/jatin/Desktop/SL/IoT/HA/Dashboard/index.html"
html= "/home/test/Desktop/SL/IoT/HA/Dashboard/index.html"

client = mqtt.Client("P1") #create new instance


class Api:
    
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def lock(self, params):
        print(str(params))
        client.connect(host)
        client.publish("lock", params)
        client.disconnect()

        if params is "0":
            print("Unlocjed ")
        if params is "1":
            #say("lights have been turned on")
            print("Locked")

    def fan(self, params):
        print(str(params))
        client.connect(host)
        client.publish("fan", params)
        client.disconnect()
        
    def switch3(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
    def switch4(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
    def switch5(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
    def switch6(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
    def switch7(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
    def switch8(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
    def switch9(self,params):
        print(str(params))
        client.connect(host)
        client.publish("switch",params)
        client.disconnect()
        
api = Api()
window = webview.create_window('API example', html, fullscreen=True, js_api=api)
webview.start(debug=True)
# mosquitto_pub -t "switch" -m "7:0"

