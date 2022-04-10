from awscrt import io, mqtt
from awsiot import mqtt_connection_builder
from csv import reader
from time import sleep
import json

ENDPOINT = "a192g7v0ycd7p2-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "touch"
PATH_TO_CERTIFICATE = "./code/operationalization/certs/touch_cert.pem.crt"
PATH_TO_PRIVATE_KEY = "./code/operationalization/certs/touch_private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "./code/operationalization/certs/touch_ca.pem"
TOPIC = "touch/events"
csv = './data/processed/touch_events.csv'

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

def reader_in_csv():
    with open(csv, 'r') as read_obj:
        now_csv = reader(read_obj)
        header = next(now_csv)
        if header != None:
            row_list = []
            for row in now_csv:
                row_list.append([str(row[0]), int(row[1])])
            return row_list
        return 'Exception Here!'

def publish_aws(mqtt_connection):
    data = reader_in_csv()
    if data:
        for row in data:
            message = {"topic": row[1], 'ds': row[0]}
            print("Sending message to AWS: {}".format(message))
            mqtt_connection.publish(topic=TOPIC,
                                    payload=json.dumps(message),
                                    qos=mqtt.QoS.AT_LEAST_ONCE
            )
            sleep(6)
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result

if __name__ == "__main__":
    mqtt_connection, connection = aws_mqtt()
    publish_aws(mqtt_connection)