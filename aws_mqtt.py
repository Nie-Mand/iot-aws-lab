from config import Config
from handler import Handler
from awscrt import mqtt, http
from awsiot import mqtt_connection_builder


class AwsMqtt:
    def __init__(self, cfg: Config, handler: Handler):
        self.cfg = cfg
        self.handler = handler

    def connect(self):
        mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=self.cfg.endpoint,
            port=8883,  # DEFAULT_PORT
            cert_filepath=self.cfg.cert_file,
            pri_key_filepath=self.cfg.key_file,
            ca_filepath=self.cfg.ca_file,
            client_id=self.cfg.client_id,
            clean_session=False,
            keep_alive_secs=30,
            http_proxy_options=None,
            on_connection_interrupted=self.handler.get_on_connection_interrupted(),
            on_connection_resumed=self.handler.get_on_connection_resumed(),
            on_connection_success=self.handler.get_on_connection_success(),
            on_connection_failure=self.handler.get_on_connection_failure(),
            on_connection_closed=self.handler.get_on_connection_closed()
        )
        self.mqtt_connection = mqtt_connection
        connect_future = mqtt_connection.connect()
        connect_future.result()
        print("[*] Connected to AWS MQTT!")

    def disconnect(self):
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()
        print("[*] Disconnected from AWS MQTT!")
