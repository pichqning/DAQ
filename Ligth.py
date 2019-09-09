from machine import Pin, ADC, PWM
from time import sleep
import math

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

led = PWM(Pin(5),freq=5000)

while True:
    voltage = sensor.read()
    print(voltage)
    d = math.ceil(voltage/4)
    print(d)
    led.duty(1023-d)
    sleep(0.1)