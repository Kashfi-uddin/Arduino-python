
import pyfirmata
from time import sleep
from pyfirmata.util import Iterator
board= pyfirmata.Arduino('COM3')


ldr=board.get_pin('a:0:i')
led=board.get_pin('d:11:p')

while True:
    value=ldr.read()
    print(value)
    led.write(value)
    sleep(1)


