from machine import Pin

pin_3v = Pin( 4 , Pin.OUT)
pin_3v.on()


# p2r =Pin( 2, Pin.IN , Pin.PULL_UP)  # GPIO 2 接板子上的 藍色 LED ，且沒有內部 pull-up 電阻
# p2r.value()                         # 所以 "無效"


p2r =Pin( 2, Pin.IN , Pin.PULL_DOWN)
p2r.value()



