from machine import Pin, ADC
from adc1_cal import ADC1Cal
import time

adc_pin = 34

ubatt = ADC1Cal( Pin( adc_pin ), 1, None, 10, "ADC1 Calibrated" ))
ubatt.width(ubatt.WIDTH_10BIT)
ubatt.atten(ubatt.ATTN_11DB) 

pin_3v = Pin( 4 , Pin.OUT)
pin_3v.on()

while True:
    print('Voltage:      {:4.1f}mV'.format( ubatt.voltage ))
    time.sleep(1)

