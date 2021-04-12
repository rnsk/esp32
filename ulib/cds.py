# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""CdS library"""

from machine import Pin, ADC

class CdS:
    def __init__(self, pin_id):
        """Initialize

        Args:
            pin_id (int): センサーのPIN番号
        """
        self.adc = ADC(Pin(pin_id))

    def read(self):
        """センサーの値を取得する

        Returns:
            integer: The return value.
        """
        return self.adc.read()

    def is_greater_than(self, expected):
        """センサーの値を比較する
        expected < value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected < self.read()

    def is_greater_than_or_equal(self, expected):
        """センサーの値を比較する
        expected <= value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected <= self.read()

    def is_less_than(self, expected):
        """センサーの値を比較する
        expected > value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected > self.read()

    def is_less_than_or_equal(self, expected):
        """センサーの値を比較する
        expected >= value が成立するかどうか

        Args:
            expected (int): 比較対象の数値
        Returns:
            bool: The return Result of comparison.
        """
        return expected >= self.read()
