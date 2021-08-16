import pyfirmata
import time
board= pyfirmata.Arduino('COM3')
led= board. get_pin('d:13:o')

while True:
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)

