# IoT program by MicroPython
# https://github.com/rnsk/micropython-iot
#
# MIT License
# Copyright (c) 2021 Yoshika Takada (@rnsk)

"""Startup script"""

import app

try:
    app.main()
except:
    print('main() function in app.py could not be executed')
