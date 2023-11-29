from handler_impl import HandlerImpl
from config import Config
from aws_mqtt import AwsMqtt


def main():
    config = Config()
    config.validate()
    handler = HandlerImpl()
    aws = AwsMqtt(config, handler)
    aws.connect()
    aws.disconnect()


# received_count = 0
# received_all_event = threading.Event()

if __name__ == '__main__':
    main()

#     message_count = cmdData.input_count
#     message_topic = cmdData.input_topic
#     message_string = cmdData.input_message

#     # Subscribe
#     print("Subscribing to topic '{}'...".format(message_topic))
#     subscribe_future, packet_id = mqtt_connection.subscribe(
#         topic=message_topic,
#         qos=mqtt.QoS.AT_LEAST_ONCE,
#         callback=on_message_received)

#     subscribe_result = subscribe_future.result()
#     print("Subscribed with {}".format(str(subscribe_result['qos'])))

#     # Publish message to server desired number of times.
#     # This step is skipped if message is blank.
#     # This step loops forever if count was set to 0.
#     if message_string:
#         if message_count == 0:
#             print("Sending messages until program killed")
#         else:
#             print("Sending {} message(s)".format(message_count))

#         publish_count = 1
#         while (publish_count <= message_count) or (message_count == 0):
#             message = "{} [{}]".format(message_string, publish_count)
#             print("Publishing message to topic '{}': {}".format(message_topic, message))
#             message_json = json.dumps(message)
#             mqtt_connection.publish(
#                 topic=message_topic,
#                 payload=message_json,
#                 qos=mqtt.QoS.AT_LEAST_ONCE)
#             time.sleep(1)
#             publish_count += 1

#     # Wait for all messages to be received.
#     # This waits forever if count was set to 0.
#     if message_count != 0 and not received_all_event.is_set():
#         print("Waiting for all messages to be received...")

#     received_all_event.wait()
#     print("{} message(s) received.".format(received_count))

#     # Disconnect
#     print("Disconnecting...")
#     disconnect_future = mqtt_connection.disconnect()
#     disconnect_future.result()
#     print("Disconnected!")
