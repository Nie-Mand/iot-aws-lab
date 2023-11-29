from awscrt import mqtt
import sys
from handler import Handler


class HandlerImpl(Handler):

    def get_on_connection_interrupted(self):
        def on_connection_interrupted(connection, error, **kwargs):
            print("Connection interrupted. error: {}".format(error))
        return on_connection_interrupted

    def get_on_connection_resumed(self):
        def on_connection_resumed(connection, return_code, session_present, **kwargs):
            print("Connection resumed. return_code: {} session_present: {}".format(
                return_code, session_present))

            if return_code == mqtt.ConnectReturnCode.ACCEPTED and not session_present:
                print("Session did not persist. Resubscribing to existing topics...")
                resubscribe_future, _ = connection.resubscribe_existing_topics()

                # Cannot synchronously wait for resubscribe result because we're on the connection's event-loop thread,
                # evaluate result with a callback instead.
                def on_resubscribe_complete(resubscribe_future):
                    resubscribe_results = resubscribe_future.result()
                    print("Resubscribe results: {}".format(resubscribe_results))

                    for topic, qos in resubscribe_results['topics']:
                        if qos is None:
                            sys.exit(
                                "Server rejected resubscribe to topic: {}".format(topic))
                resubscribe_future.add_done_callback(on_resubscribe_complete)

    def get_on_connection_success(self):
        def on_connection_success(connection, callback_data):
            assert isinstance(callback_data, mqtt.OnConnectionSuccessData)
            print("Connection Successful with return code: {} session present: {}".format(
                callback_data.return_code, callback_data.session_present))
        return on_connection_success

    def get_on_connection_failure(self):
        def on_connection_failure(connection, callback_data):
            assert isinstance(callback_data, mqtt.OnConnectionFailureData)
            print("Connection failed with error code: {}".format(
                callback_data.error))
        return on_connection_failure

    def get_on_connection_closed(self):
        def on_connection_closed(connection, callback_data):
            print("Connection closed")
        return on_connection_closed

    def get_on_message_received(self):
        def on_message_received(topic, payload, dup, qos, retain, **kwargs):
            print("Received message from topic '{}': {}".format(topic, payload))
        return on_message_received
