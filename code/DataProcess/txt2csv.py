# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:36:40 2020

@author: ASUS
"""

import csv

# not dict
with open('data-sensor.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    # 读要转换的txt文件，文件每行各词间以字符分隔
    with open('data-sensor.txt', 'r') as filein:
        count = 0
        for line in filein:
            if count == 0:
                line = line.replace('"','')
            line_list = line.strip('\n').split(',')   #我这里的数据之间是以 , 间隔的
            spamwriter.writerow(line_list)
            count += 1
# dict
with open('data-sensor.csv', 'w+', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    with open('data-sensor.txt','r') as filein:
        count = 0
        for line in filein:
            line_dict = eval(line)
            line_list = line_dict['payload'].split(',')
            spamwriter.writerow(line_list)
            count += 1

'''        
data = lines[1]
b = eval(data)

f3 = b['payload']

with open('data-sensor.txt','r') as filein:
    f1 = filein.readline()
    f2 = filein.readline()

with open('raw-data-sensor.txt','r') as data_file:
        count = 0
        for line in filein:
            line_dict = eval(line)
            line_list = line_dict['payload'].split(',')
            spamwriter.writerow(line_list)
            count += 1
'''