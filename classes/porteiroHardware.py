from machine import Pin,reset

class Trava():

    def __init__(self):

        #self.PINS = [4,13,12,15] #teste no wity
        self.PINS = [12,15,13,16]
        self.botao = Pin(self.PINS[0], Pin.IN,Pin.PULL_UP) #change pin for pin 12, teste [4,13,12,15]
        self.rele = Pin(self.PINS[1],Pin.OUT) #15
        self.led_verde = Pin(self.PINS[2],Pin.OUT)#13
        self.led_red = Pin(self.PINS[3],Pin.OUT)#16

    def door(self, status):
        """
        this method just chang the led's pins value and rele's pin.
        """
        try:
            self.rele.value(not(status))
            self.led_red.value(not(status))
            self.led_verde.value(status)    
        except :
            print('error in method door')

    def ldc(self):
            print('not implemented yet')