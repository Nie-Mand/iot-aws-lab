from connection_handler_impl import ConnectionHandlerImpl
from config import Config
from aws_mqtt import AwsMqtt
import time


TOPIC = "sdk/test/python"


def on_message_received(topic, payload, dup, qos, retain, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    # if received_count == cmdData.input_count:
    #     received_all_event.set()


def main():
    config = Config()
    config.validate()
    connection_handler = ConnectionHandlerImpl()
    aws = AwsMqtt(config, connection_handler)
    aws.connect()
    aws.subscribe(TOPIC, on_message_received)

    for i in range(10):
        msg = {"index": i, "hello": "world"}
        time.sleep(2)
        aws.publish(TOPIC, msg)

    aws.disconnect()



if __name__ == '__main__':
    main()
