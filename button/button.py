import pyfirmata
from pyfirmata.util import Iterator

board = pyfirmata.Arduino('COM3')
ite=Iterator(board)
ite.start()
button= board.get_pin('d:2:i')
led= board.get_pin('d:12:o')
 

while True:
    if button.read()== 1:
        led.write(1)
    else:
        led.write(0)    
