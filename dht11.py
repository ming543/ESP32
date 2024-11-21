from machine import Pin

pin_3v = Pin( 4 , Pin.OUT)
pin_3v.on()

pin_up =Pin( 13, Pin.IN , Pin.PULL_UP)


import machine, dht

dht11=dht.DHT11(machine.Pin(12))


while True:
  dht11.measure()
  print('攝氏:      {:4.1f}度C'.format( dht11.temperature() ))
  print('濕度:      {:4.1f}％'.format( dht11.humidity() ))
  if pin_up.value() == 0 :
     break
  time.sleep(1)


