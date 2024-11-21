from machine import Pin
import time

led = Pin(2,Pin.OUT)
b_1 = Pin( 13, Pin.IN , Pin.PULL_UP)
b_2 = Pin( 14, Pin.IN , Pin.PULL_UP)
b_3 = Pin( 15, Pin.IN , Pin.PULL_UP)
b_4 = Pin( 16, Pin.IN , Pin.PULL_UP)
led_states = 0
b_1_states = 0

while True:
    time.sleep(1)    
    if b_1_states != b_1.value(): # 如果開關讀值與儲存狀態不同
        b_1_states = ~b_1_states & 1 # 將開關狀態反向
        time.sleep(0.2) # debounce
        led_states = ~led_states & 1 # LED狀態反向
    led.value(led_states) #LED ON/OFF由led_states變數決定
    

