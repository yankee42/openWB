#!/usr/bin/env python
#coding: utf8

import time
import RPi.GPIO as GPIO
import sys

onOff = str(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.OUT)

f = open('/var/www/html/openWB/ramdisk/socketActivated', 'w')

if (onOff == "on"):
    GPIO.output(15, GPIO.HIGH)
    f.write(str(1))
elif (onOff == "off"):
    GPIO.output(15, GPIO.LOW)
    f.write(str(0))
else:
    print("Invalid argument: '" + onOff + "'. Supporting only [on,off]")

f.close()
