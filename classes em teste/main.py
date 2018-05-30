from porteiroClasse import*
from os import remove ,listdir
import time

time.sleep(3)

MATRICULAS = []
                              
porteiro = Porteiro('0.0.0.0',8011)
porteiro.idsSetting(MATRICULAS,tags = "", who = 0)
porteiro.setConnection()
porteiro.run()

