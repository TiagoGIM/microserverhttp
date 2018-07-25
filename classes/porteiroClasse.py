import time
from machine import Pin,reset
from classes.botaoWeb import BotaoWeb
from classes.porteiroHardware import Trava
from classes.menu import Menu
import gc

class Porteiro(BotaoWeb,Trava, Menu):
    kind = 'Classe principal da porta'
    
    def __init__(self,virtual):
        print('init Porteiro main')
#qnd trava tem botao virtual
        self.statusServer = False
# fim da trava virtual

        Trava.__init__(self)
        #variable for checking wich the last time the port was acionated
        self.press = time.time()
        self.status_porta = True
        #usada pra resetar o esp de tempos em tempos, para previnir crash no sistema
        self.time_to_reset_esp = time.time()

        self.tags = []
        self.matriculas = []

    def idsSetting(self, matricula, tags = None,who=0):
        #load ids enabled for acess the door
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

#seting botao web
    def startServerButton(self,port,host,wifi_setings):
        print('starting webButton')
        self.serverWeb = BotaoWeb(port,host,wifi_setings)        
        self.statusServer = self.serverWeb.setConnection()

    def botaoVirtual(self):        
        self.serverWeb.botaoWeb(self.openDoor,self.matriculas)
#fim botaoWeb

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
    def menuUser(self):
        x = input('enter comand [i = print ip network, d = reset, x = exit loop, m = aberta permanente] >>')
        if x == 'd':
            reset()
        elif x == 'x':
            self.loop = False
        elif x == 'm':
            self.manutencao()                    
        elif x == 'i':
            if self.statusServer:                
                self.serverWeb.networkIp()
            else:
                print('server its not enabled.')
        else:
            pass

    def run(self):
        self.loop = True 
        while self.loop:
            #self.preventBughu3hu3(5*60)
            try:
                #2 = tempo para fechar a porta                 
                self.porteiro(2)
                self.botaoReal()
                if self.statusServer:
                    self.botaoVirtual()
                gc.collect()
            except KeyboardInterrupt:
                try:
                    self.menuUser()
                except :
                    print('iji')