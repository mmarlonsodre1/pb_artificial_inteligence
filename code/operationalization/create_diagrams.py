from diagrams.aws.iot import IotCar, IotCore, IotMqtt, IotAnalyticsChannel, IotAnalyticsPipeline, IotAnalyticsDataSet, IotAnalyticsDataStore
from diagrams import Cluster, Diagram

with Diagram('Projeto', show=False) as diag:
    with Cluster("Edge"):
        touch = IotCar('touch')
        mqtt = IotMqtt('pub/sub \n (touch/events)')
    with Cluster('Cloud'):
        iotcore = IotCore("IotCore")
        with Cluster('AWS Analytics'):
            channel = IotAnalyticsChannel('Channel')
            pipeline = IotAnalyticsPipeline('Pipeline')
            datastore = IotAnalyticsDataStore('DataStore')
            dataset = IotAnalyticsDataSet('Dataset')

    touch >> mqtt >> iotcore >> channel >> pipeline >> datastore >> dataset

diag