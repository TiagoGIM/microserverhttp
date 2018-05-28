from porteiroClasse import*

MATRICULAS = []
                              
porteiro = Porteiro('0.0.0.0',8015)
porteiro.idsSetting(MATRICULAS,tags = "", who = 0)
porteiro.setConnection()
porteiro.networkIp()
porteiro.run()

