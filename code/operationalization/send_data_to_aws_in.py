from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
from csv import reader
from time import sleep
import json

ENDPOINT = "a192g7v0ycd7p2-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "touch"
# USER_PATH = '/Users/marlonsodre/Desktop/Develop.nosync/Python/pb_artificial_inteligence'
PATH_TO_CERTIFICATE = "./code/operationalization/certs/touch.cert.pem"
PATH_TO_PRIVATE_KEY = "./code/operationalization/certs/touch.private.key"
PATH_TO_AMAZON_ROOT_CA_1 = "./code/operationalization/certs/root-CA.crt"
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

    return connect_future

def reader_in_csv():
    with open(csv, 'r') as read_obj:
        now_csv = reader(read_obj)
        header = next(now_csv)
        if header != None:
            for row in now_csv:
                print(int(row[3]))
                content = int(row[3])
                sleep(1)
                return content
        return 'Exception Here!'

def publish_aws():
    data = reader_in_csv()
    if data:
        message = {"topic": data}
        print("Sending message to AWS: {}".format(data))
        mqtt_connection.publish(topic=TOPIC,
                                payload=json.dumps(message),
                                qos=1)
        t.sleep(.1)
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result

if __name__ == "__main__":
    while True:
        mqtt_connection = aws_mqtt()
        publish_aws()
        t.sleep(4)