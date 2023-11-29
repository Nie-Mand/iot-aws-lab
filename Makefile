# SETUP SCRIPTS

validate:
	@echo -e "\033[0;32m[*] Make sure you have python3 installed.\033[0m"
	@echo -e "\033[0;32m[*] Make sure you have the required connection files in the root directory.\033[0m"
	@echo -e "\033[0;32m[*] The Required files are:\033[0m"
	@echo -e "\033[0;32m\t- [x] THING-NAME.cert.pem\033[0m"
	@echo -e "\033[0;32m\t- [x] THING-NAME.private.key\033[0m"
	@echo -e "\033[0;32m\t- [x] THING-NAME.public.key\033[0m"
	@echo -e "\033[0;32m\t- [x] THING-NAME-Policy\033[0m"

venv:
	@echo -e "\033[0;32m[*] Creating virtual environment...\033[0m"
	@python3 -m venv venv

root-CA.crt:
	@echo -e "\033[0;32m[*] Downloading AWS IoT Root CA certificate from AWS...\033[0m"
	@curl https://www.amazontrust.com/repository/AmazonRootCA1.pem > root-CA.crt

aws-iot-device-sdk-python-v2:
	@echo -e "\033[0;32m[*] Cloning the AWS SDK...\033[0m"
	@git clone https://github.com/aws/aws-iot-device-sdk-python-v2.git --recursive

awsiot:
	@echo -e "\033[0;32m[*] Installing AWS IoT Device SDK...\033[0m"
	@./venv/bin/pip install ./aws-iot-device-sdk-python-v2
	@./venv/bin/pip install -r requirements.txt

setup: validate venv root-CA.crt aws-iot-device-sdk-python-v2 awsiot
	@echo -e "\033[0;32m[*] Setup complete!\033[0m"

run: venv
	@echo -e "\033[0;32m[*] Starting development server...\033[0m"
	@./venv/bin/python main.py

# Phonies
.PHONY: setup run validate awsiot