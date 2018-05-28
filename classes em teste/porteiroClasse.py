from time import sleep, time
from machine import Pin,reset
from botaoWeb import*

class Porteiro(BotaoWeb):
    kind = 'Classe principal da porta'

    def __init__(self,port,host):

        BotaoWeb.__init__(self,port,host)
        # self.porteiroWeb = BotaoWeb(port,host)

        self.botao = Pin(12, Pin.IN,Pin.PULL_UP)
        self.rele = Pin(15,Pin.OUT)
        self.led_verde = Pin(13,Pin.OUT)
        self.led_red = Pin(16,Pin.OUT)

        #variable for checking wich the last time the port was acionated
        self.press = time()
        self.status_porta = True
        #usada pra resetar o esp de tempos em tempos, para previnir crash no sistema
        self.time_to_reset_esp = time()
        self.tags = []
        self.MATRICULAS = []

    def idsSetting(self, matricula, tags,who=0):
        if who == 0:
            self.MATRICULAS = matricula
        else:
            self.tags = tags

    def door(self, status):
        """
        this method just chang the led's pins value and rele's pin.
        """
        try:
            self.rele.value(status)
            self.led_red.value(not(status))
            self.led_verde.value(status)    
        except :
            print('error in method door')

    def openDoor(self):
        self.press = time()
        print('"press" att')

    def pushButton(self):
        try:
            if not(self.botao.value()):
                self.openDoor()
            else:
                pass
        except :
            print('troble pushButton')
            pass
    def porteiro(self, tempo):
        """
        this method compare which the last time the door() was
        used and wich is the status_porta for so att the status_porta
        """
        elapsed = time() - self.press
        try:
            if elapsed > tempo and self.status_porta:
                self.door(0)
                self.status_porta = False
                print('fechar')
            elif elapsed < tempo and not self.status_porta:
                self.door(1)
                self.status_porta = True
                print('abrir')
            else:
                print('e ai?')

        except :
            print('error >> porteiro()')

    def manutencao(self):
        self.door(1)
        input('press keyboard for restart loop')
        print("run()")

    def preventBughu3hu3(self, time_for_reset):
        "this method just "
        if (time() - self.time_to_reset_esp > (time_for_reset)):
            reset() #reset esp
            self.time_to_reset_esp = time()
        else:
            pass


    def run(self):

        loop = True

        while loop:
            self.preventBughu3hu3(15*60)
            self.porteiro(2)
            self.pushButton()
            
            
            try:
                self.botaoWeb(self.openDoor(),self.MATRICULAS)
             
            except:
                x = input('enter comand [d = reset, x = exit loop, m = aberta permanente] >>')
                if x == 'd':
                    reset()
                elif x == 'x':
                    print('X')
                    loop = False
                elif x == 'm':
                    self.manutencao()