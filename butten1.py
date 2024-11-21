from machine import Pin
import time

pin_3v = Pin( 4 , Pin.OUT)
pin_3v.on()

pin_down =Pin( 13, Pin.IN , Pin.PULL_DOWN)
pin_down.value()


pin_down.value()


while True:
  print( pin_down.value() )
  time.sleep(0.5)

