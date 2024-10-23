#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()


def write(text):
    print("Now place your tag to write")
    reader.write(text)
    print("Written")


def read():
    data = reader.read()
    return data


def cleanup():
    GPIO.cleanup()
