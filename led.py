from machine import Pin
from time import sleep

sw = Pin(22, Pin.IN)
led = Pin(23, Pin.OUT)

check = 0
while True:
    print("Switch value = ", sw.value())
    while sw.value() == 1:
        pass

    led.value(check)
    if check == 0:
        check = 1
    else:
        check = 0

    while sw.value() == 0:
        pass

    sleep(0.5)
   

            
