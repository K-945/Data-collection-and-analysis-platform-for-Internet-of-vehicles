# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:28:04 2020

@author: ASUS
"""
 
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt 

class MqttClient:
       
    def __init__(self, host, port, mqttClient):
        self._host = host
        self._port = port
        self._mqttClient = mqttClient

    # 连接MQTT服务器
    def on_mqtt_connect(self, username="tester", password="tester"):
        self._mqttClient.username_pw_set(username, password)
        self._mqttClient.connect(self._host, self._port, 60)
        self._mqttClient.loop_start()
     
    # publish 消息
    def on_publish(self, topic, msg, qos):
        self._mqttClient.publish(topic, msg, qos)
     
    # 消息处理函数
    def on_message_come(client, userdata, msg):
        print(msg.topic + " " + ":" + str(msg.data))
     
    # subscribe 消息
    def on_subscribe(self, topic):
        self._mqttClient.subscribe(topic, 1)
        self._mqttClient.on_message = self.on_message_come # 消息到来处理函数
'''     
    def main():
        self.on_mqtt_connect()
        on_publish("/test/server", "Hello Python!", 1)
        self.on_subscribe()
        print("connect success!\n")
        while True:
            pass
'''
 
if __name__ == '__main__':
#    main()
    host = "localhost"
    port = 1883
    #topic = "CarTest"
    topic = "user3"
#    msg = "Hello Python!"
    qos = 1
    username = "tester"
    password = "tester"
    mqttClient = mqtt.Client("tester")
    
    client = MqttClient(host, port, mqttClient)
    client.on_mqtt_connect(username, password)
#    client.on_publish(topic, msg, qos)
    client.on_subscribe(topic)
    

    # 多客户端连接
    mqttClient_2 = mqtt.Client("tester-2")
    username_2 = username + '2'
    password_2 = password + '2'
    client_2 = MqttClient(host, port, mqttClient_2) 
    client_2.on_mqtt_connect(username_2, password_2)
    client_2.on_subscribe(topic)

    mqttClient_3 = mqtt.Client("tester-3")
    username_3 = username + '3'
    password_3 = password + '3'
    client_3 = MqttClient(host, port, mqttClient_3) 
    client_3.on_mqtt_connect(username_3, password_3)
    client_3.on_subscribe(topic)

    with open('sensor_data-Copy1.csv', 'r') as f:
       #  next(f) # skip header line
       count = 0
       for line in f:
           msg = line.rstrip().encode()
           client.on_publish(topic, msg, qos)
#       producer.send('creditcard-test-0', line.rstrip().encode())
           count += 1
       print(count, "records has been produced in 'CarTest'")
 
    
    
    print("connect success!\n")
    
    
    while True:
        pass
    
    
