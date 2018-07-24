from porteiroHardware import Trava

class Menu(Trava):
    kind = 'menu de funcoes admin'
 
    def manutencao(self):
        self.door(1)
        input('press keyboard for restart loop')
        self.door(0)

