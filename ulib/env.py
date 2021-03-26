# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""ENV library"""

import dht
from machine import Pin

class ENV:
    def __init__(self, pin_id, env_type):
        """Initialize

        Args:
            pin_id (int): センサーのPIN番号
            env_type (str): センサーの種別（temperature, humidity）
        """
        self.env_type = env_type

        if self.env_type in {'temperature', 'humidity'}:
            self.sensor = dht.DHT11(Pin(pin_id))

    def read_data(self):
        """センサーの値を取得する

        Returns:
            integer: The return value.
        """
        if self.env_type == 'temperature':
            self.sensor.measure()
            return self.sensor.temperature() # eg. 23 (°C)

        if self.env_type == 'humidity':
            self.sensor.measure()
            return self.sensor.humidity() # eg. 41 (% RH)

    def is_greater_than(self, expected):
        """センサーの値を比較する
        expected < value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected < self.read_data()

    def is_greater_than_or_equal(self, expected):
        """センサーの値を比較する
        expected <= value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected <= self.read_data()

    def is_less_than(self, expected):
        """センサーの値を比較する
        expected > value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected > self.read_data()

    def is_less_than_or_equal(self, expected):
        """センサーの値を比較する
        expected >= value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected >= self.read_data()
