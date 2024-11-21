from machine import Pin
led=Pin(2,Pin.OUT)
led.value(1)
led.value(0)

import time
while True:
    led.value(1)
    time.sleep(1.5)
    led.value(0)
    time.sleep(1.5)

