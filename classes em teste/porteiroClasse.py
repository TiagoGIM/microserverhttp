import time
from machine import Pin,reset
from botaoWeb import BotaoWeb
from porteiroHardware import Trava
from menu import Menu
import gc

class Porteiro(BotaoWeb,Trava, Menu):
    kind = 'Classe principal da porta'
    
    def __init__(self,port,host):
        BotaoWeb.__init__(self,port,host)
        Trava.__init__(self)
        #variable for checking wich the last time the port was acionated
        self.press = time.time()
        self.status_porta = True
        #usada pra resetar o esp de tempos em tempos, para previnir crash no sistema
        self.time_to_reset_esp = time.time()

        self.tags = []
        self.matriculas = []

    def idsSetting(self, matricula, tags = None,who=0):
        if who == 0:
            self.matriculas = matricula
        else:
            self.tags = tags

    def openDoor(self):
        self.press = time.time()
        print('"press" att')

    def botaoReal(self):
        try:
            if not(self.botao.value()):
                self.openDoor()
            else:
                pass
        except :
            print('troble botaoReal')
            pass

    def porteiro(self, tempo):
        """
        this method compare which the last time the door() was
        used and wich is the status_porta for so att the status_porta
        """
        elapsed = time.time() - self.press
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
                pass

        except :
            print('error >> porteiro()')

    def preventBughu3hu3(self, time_for_reset):
        "this method just "
        if (time.time() - self.time_to_reset_esp > (time_for_reset)):
            reset() #reset esp
            self.time_to_reset_esp = time.time()
        else:
            pass

    def run(self):
        loop = True
        while loop:
            #self.preventBughu3hu3(5*60)
            try:
                
                self.porteiro(2)
                self.botaoReal()        
                self.botaoWeb(self.openDoor,self.matriculas)
                gc.collect()

            except KeyboardInterrupt:
                try:
                    x = input('enter comand [i = print ip network, d = reset, x = exit loop, m = aberta permanente] >>')
                    if x == 'd':
                        reset()
                    elif x == 'x':
                        loop = False
                    elif x == 'm':
                        self.manutencao()                    
                    elif x == 'i':                
                        self.networkIp()
                except :
                    print('iji')