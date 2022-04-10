from awscrt import io, mqtt
from awsiot import mqtt_connection_builder, iotshadow
import threading

ENDPOINT = "a192g7v0ycd7p2-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "subscribe_touch"
THING_NAME = "touch"

PATH_TO_CERTIFICATE = "./code/operationalization/certs/touch_cert.pem.crt"
PATH_TO_PRIVATE_KEY = "./code/operationalization/certs/touch_private.pem.key"
PATH_TO_AMAZON_ROOT_CA_1 = "./code/operationalization/certs/touch_ca.pem"
TOPIC = "$aws/things/touch/shadow/update"

received_count = 0
received_all_event = threading.Event()


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
    )
    connect_future = mqtt_connection.connect()
    shadow_client = iotshadow.IotShadowClient(mqtt_connection)
    connect_future.result()

    return mqtt_connection, connect_future, shadow_client


def on_message_received(delta):
    global received_count
    try:
        received_count += 1
        event = delta.state['topic']
        if event == '0':
            print('Interruptor de ventilador pressionado (* Ligando ou Desligando Ventilador *)')
        if event == '1':
            print('Interruptor de luz pressionado (* Ligando ou Desligando Luz *)')
        if event == '2':
            print('Interruptor de porta pressionado (* Desbloqueando porta *)')
        if received_count == 100:
            received_all_event.set()
    except:
        print("Evento topic repetido")


def subscribe_aws(mqtt_connection, shadow_client):
    delta_subscribed_future, _ = shadow_client.subscribe_to_shadow_delta_updated_events(
        request=iotshadow.ShadowDeltaUpdatedSubscriptionRequest(thing_name=THING_NAME),
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_received
    )
    delta_subscribed_future.result()

    received_all_event.wait()
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()


if __name__ == "__main__":
    mqtt_connection, connection, shadow_client = aws_mqtt()
    subscribe_aws(mqtt_connection, shadow_client)
