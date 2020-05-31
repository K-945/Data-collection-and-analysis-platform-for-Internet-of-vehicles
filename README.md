# Data-collection-and-analysis-platform-for-Internet-of-vehicles
MQTT+Kafka+KSQL+Tensorflow

本平台的构建笔记：https://blog.csdn.net/qq_41094332/article/details/106223143

## 构建完各个配置软件后，所需的代码在`code`文件当中。

[1] `mqtt_client`中含有汽车传感器模拟数据文件和MQTT客户端的构建代码。
`mqtt_client.py`实现了创建三个MQTT客户端，读取`sensor_data-Copy1.csv`文件，发送数据给MQTT Broker。

[2] `DataProcess`中含有获取Kafka中数据到本地，转换数据文件格式，数据处理构建模型预测的代码。

* 首先，使用`kafka-consumer.py`从Kafka中获取数据保存至`data-sensor.txt`文件当中。
* 然后，使用`txt2csv.py`将数据转换成`.csv`格式，其中若所传输的数据为非字典的格式，则使用#not dict。若所传输的数据为字典格式，则使用#dict。
* 最后，使用`ipython-lstm-train.ipynb`来进行数据分析，构建模型，预测数据。
