# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:03:00 2020

@author: ASUS
"""

from kafka import KafkaConsumer
from kafka.structs import TopicPartition

consumer = KafkaConsumer('creditcard-test-0',
                         bootstrap_servers='localhost:9092',
                         group_id='creditcard',
                         auto_offset_reset='earliest')

print('consumer start to consuming...')
consumer.subscribe(('creditcard-test-0', ))
consumer.seek(TopicPartition(topic='creditcard-test-0', partition=0), 0)

filename = 'data-sensor.txt'
output = open(filename,'w')

for message in consumer:
#    print(message.topic, message.offset, message.key, message.value, message.value, message.partition)
    print(bytes.decode(message.value))
    output.write(bytes.decode(message.value))
    output.write("\n")
    count += 1
    if count == 10001:
        break
output.close()   
print("================================")
print("message: %d" %(count))


'''
msg = consumer.poll(timeout_ms=3)
print(msg["values"])
list(msg.keys())
output = open('data.txt','w')
output.write(msg.values())
'''


