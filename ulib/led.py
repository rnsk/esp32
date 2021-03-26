# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""LED library"""

import time
from machine import Pin

class LED:
    def __init__(self, pin_id):
        """Initialize

        Args:
            pin_id (int): LEDのPIN番号
        """
        self.pin = Pin(pin_id, Pin.OUT)

    def light_on(self):
        """LED点灯

        Returns:
            void
        """
        self.pin.on()

    def light_off(self):
        """LED消灯

        Returns:
            void
        """
        self.pin.off()

    def blink(self, delay = 500):
        """LED点滅

        Args:
            delay (int): 点滅の間隔（ミリ秒）
        Returns:
            void
        """
        self.pin.on()
        time.sleep_ms(delay)
        self.pin.off()
        time.sleep_ms(delay)
