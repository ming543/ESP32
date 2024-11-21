
# https://docs.micropython.org/en/v1.18/esp32/tutorial/pwm.html#esp32-pwm

from machine import Pin, PWM
try:
    f = 1000  # Hz
    d = 1024 // 16  # 6.25%
    pins = (15, 2, 4, 16, 18, 19, 22, 23, 25, 26, 27, 14 , 12, 13, 32, 33)
    pwms = []
    for i, pin in enumerate(pins):
        pwms.append(PWM(Pin(pin), freq=f * (i // 2 + 1), duty= 1023 if i==15 else d * (i + 1)))
        print(pwms[i])
finally:
    for pwm in pwms:
        try:
            pwm.deinit()
        except:
            pass


# https://docs.micropython.org/en/v1.18/esp32/quickref.html#pwm-pulse-width-modulation
'''
兩組速度模式 ( mode ) ， 0:LOW_SPEED_MODE ，1:LOW_SPEED_MODE
每組 mode 有 8 個 Channel 、4 個 Timer 
ESP32 的最大 PWM 通道（Pin）數量 : 16 個通道，但只有 8 個不同的 PWM 頻率可用，其餘 8 個通道必須具有相同的頻率。
另一方面，在相同頻率下可能有 16 個獨立的 PWM 佔空比。
'''

