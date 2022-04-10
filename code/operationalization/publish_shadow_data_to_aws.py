import pandas as pd
from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
from time import sleep

import json

ENDPOINT = "a192g7v0ycd7p2-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "publish_touch"
PATH_TO_CERTIFICATE = "./code/operationalization/certs/touch_cert.pem.crt"
PATH_TO_PRIVATE_KEY = "./code/operationalization/certs/touch_private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "./code/operationalization/certs/touch_ca.pem"
TOPIC = "$aws/things/touch/shadow/update"

df = pd.read_csv('./data/processed/touch_events.csv')
df['ds'] = df['time']
df['time'] = pd.to_datetime(df['time'])
df.set_index(['time'], inplace=True)
df.sort_index(inplace=True)


def aws_mqtt():
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERTIFICATE,
        pri_key_filepath=PATH_TO_PRIVATE_KEY,
        client_bootstrap=client_bootstrap,
        ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=6
    )
    connect_future = mqtt_connection.connect()
    connect_future.result()

    return mqtt_connection, connect_future


def publish_aws(mqtt_connection):
    for x in range(len(df['class'].values)):
        message = {"state": {"desired": {"ds": df['ds'][x], "topic": str(df['class'][x])}}}
        print("Sending message to Shadow AWS: {}".format(message))
        mqtt_connection.publish(
            topic=TOPIC,
            payload=json.dumps(message),
            qos=mqtt.QoS.AT_MOST_ONCE
        )
        sleep(4)
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result


if __name__ == "__main__":
    mqtt_connection, connection = aws_mqtt()
    publish_aws(mqtt_connection)
