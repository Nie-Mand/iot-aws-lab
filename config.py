from dotenv import dotenv_values
import sys
import os


class Config:
    endpoint = ""
    ca_file = ""
    cert_file = ""
    key_file = ""
    client_id = ""

    def __init__(self):
        config = dotenv_values(".env")
        self.endpoint = self._load_key(config, "ENDPOINT")
        self.ca_file = self._load_key(config, "CA_FILE")
        self.cert_file = self._load_key(config, "CERT_FILE")
        self.key_file = self._load_key(config, "KEY_FILE")
        self.client_id = self._load_key(config, "CLIENT_ID")

    def _load_key(self, config, key):
        try:
            value = config[key]
            if value == "":
                raise ValueError
        except:
            print("Missing value for {}".format(key))
            sys.exit(2)
        return value

    def validate(self):
        # does self.ca_file exists
        if not os.path.isfile(self.ca_file):
            print("CA_FILE does not exist")
            sys.exit(2)
        # does self.cert_file exists
        if not os.path.isfile(self.cert_file):
            print("CERT_FILE does not exist")
            sys.exit(2)
        # does self.key_file exists
        if not os.path.isfile(self.key_file):
            print("KEY_FILE does not exist")
            sys.exit(2)
        # does self.client_id exists
        if self.client_id == "":
            print("CLIENT_ID is empty")
            sys.exit(2)
