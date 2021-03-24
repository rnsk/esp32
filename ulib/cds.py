# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""CdS library"""

from machine import Pin, ADC

class CdS:
    def __init__(self, pin_id):
        self.adc = ADC(Pin(pin_id))

    def read_data(self):
        """センサの値を取得する

        Returns:
            integer: The return value.
        """
        return self.adc.read()
