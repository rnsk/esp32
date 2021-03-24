# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""Application script"""

import config
import time
import ujson

publish_interval = 10 # データ送信間隔（秒）

def do_connect(ssid, password):
    """WiFi に接続する

    Args:
        ssid (str): 接続するSSID
        password (str): 接続するパスワード
    """
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

def do_publish(topic, message):
    """MQTT で送信する

    Args:
        topic (str): 送信先トピック名
        messaage (str): 送信するメッセージ
    Example:
        $ mosquitto_sub -v -t topic -h localhost -p 1883
        topic {"devicename": "ESP32", "value": "データ", "deviceid": "001"}
    """
    from ulib.umqtt import MQTTClient
    client = MQTTClient(config.DEVICE_ID, config.MQTT_HOST, config.MQTT_PORT)
    client.connect()
    client.publish(bytearray(topic), bytearray(message))
    time.sleep(1)
    client.disconnect()

def main():
    ssid = config.WIFI_SSID
    password = config.WIFI_PASSWORD

    do_connect(ssid, password)
    time.sleep(5)

    from ulib.cds import CdS
    cds = CdS(config.CDS_PIN)

    while True:
        value = cds.read_data()
        data = {
            "deviceid": config.DEVICE_ID,
            "devicename": config.DEVICE_NAME,
            "value": value
        }
        payload = ujson.dumps(data)

        try:
            do_publish(config.MQTT_TOPIC, payload)
        except:
            pass

        time.sleep(publish_interval)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
