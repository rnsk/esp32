# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""App configration"""

# wifi setting
# config.WIFI_xxx
WIFI_SSID = ''
WIFI_PASSWORD = ''

# Device setting
# config.DEVICE_xxx
DEVICE_ID = ''
DEVICE_NAME = ''

# MQTT setting
# config.MQTT_xxx
MQTT_HOST = 'localhost'
MQTT_PORT = 1883
MQTT_USER = ''
MQTT_PASS = ''
MQTT_TOPIC = ''

# CdS setting
# config.CDS_xxx
# ADC Pins 32-39
CDS_PIN = 32
CDS_EXPECTED = 100

# ENV setting
# config.ENV_xxx
# Available Pins 0, 2, 4, 5, 12, 13, 14, 15, 16.
ENV_TEMPERATURE_PIN = 14
ENV_HUMIDITY_PIN = 14

# LED setting
# config.LED_xxx
# Available Pins 0-19, 21-23, 25-27, 32-39
LED_PIN = 12
