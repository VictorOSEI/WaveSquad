
import paho.mqtt.client as mqtt
import time


def fast(message):
        lcd.write_string(message.payload)
        time.sleep(5)
        lcd.clear()



def on_message(client, userdata, message):
        print message.payload




def on_connect(client, userdata, flags, code):
        print "connected:" + str(code)
        client.subscribe("text/all")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

#lcd.write_string("Need Help Here")



client.loop_forever()
