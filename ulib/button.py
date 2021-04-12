# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""Button library"""

from utime import ticks_ms
from machine import Pin

class Button:
    def __init__(self, pin_id, delay_time=50):
        """Initialize

        Args:
            pin_id (int): ボタンのPIN番号
        """
        self.pin = Pin(pin_id, Pin.IN, Pin.PULL_UP)
        self.pin.irq(handler=self.on_interrupt, trigger=(Pin.IRQ_FALLING|Pin.IRQ_RISING))

        self.start_ticks = 0
        self.last_ticks = 0
        self.last_state = False
        self.delay_time = delay_time

    def on_interrupt(self, pin):
        """割り込み処理

        Args:
            pin (object): Pin インスタンス
        """
        if self.pin == pin:
            pin_val = pin.value()

            # FALLING
            if pin_val == 0:
                if ticks_ms() - self.last_ticks > self.delay_time:
                    self.last_state = True
                    self.start_ticks = ticks_ms()

            # RISING
            elif pin_val == 1:
                if self.last_state == True:
                    self.last_state = False

            self.last_ticks = ticks_ms()

    def read(self):
        """ボタンの値を取得する

        Returns:
            integer: The return value, 0 or 1.
        """
        return not self.pin.value()

    def isPressed(self):
        """ボタンが押されていることの確認

        Returns:
            integer: The return value, 0 or 1.
        """
        return self.read()

    def isReleased(self):
        """ボタンが押されていないことの確認

        Returns:
            integer: The return value, 0 or 1.
        """
        return not self.read()

    def pressedFor(self, timeout):
        """長押しされていることの確認

        Args:
            timeout (int): タイムアウトの時間（ミリ秒）
        Returns:
            boolean: True if applicable, False otherwise
        """
        if self.last_state and ticks_ms() - self.start_ticks > timeout * 1000:
            return True
        else:
            return False
