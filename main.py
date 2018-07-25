from classes.porteiroClasse import Porteiro
from os import remove ,listdir
import time

time.sleep(3)

MATRICULAS = ['123']

wifi_config = {
    'pw' :'12345678g',
    'ssid':'12345678g'
}

porteiro = Porteiro(1)
porteiro.idsSetting(MATRICULAS,tags = "", who = 0)

porteiro.startServerButton('0.0.0.0',8011,wifi_config)
porteiro.run()
