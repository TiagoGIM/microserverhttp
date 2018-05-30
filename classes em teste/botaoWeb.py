import socket 
import uselect
import network
from db import Datapages


class BotaoWeb(Datapages):
    kind = 'Classe do botao virtual'

    def __init__(self, port, host):
        self.w = network.WLAN(network.STA_IF)
        self.w.active(True)
        self.port = port
        self.host = host

        self.poller = uselect.poll()


        Datapages.__init__(self,'teste')
        self.openDB()
        self.msgWeb = self.openPage('home')
        self.dbClose()
        self.bancoClose()

    
    def networkIp(self):        
        print(self.w.ifconfig())
        input('press keyboard for skip this method')

    def closeSock(self):
        self.s.close()  

    def setConnection(self):
        self.addr = socket.getaddrinfo(self.port, self.host)[0][-1]
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.poller.register(self.s, uselect.POLLIN)
        self.s.bind(self.addr)
        self.s.listen(1)
        print('listening on', self.addr)

    def botaoWeb(self,func,m):
        #try:
            res = self.poller.poll(30)
            if not res:
                pass
            else:
                cl, addr = self.s.accept()
                request = cl.recv(1023)                
                method , request = self.tratamentoGet(request)

                if method == 'GET':
                    if request:
                        response = self.msgWeb+'\n'
                        if request =='/':
                            print('send response page home')                        
                            cl.send(response)
                            cl.close()
                        elif request.find("Matricula") > 0:
                            matricula = request.split("=")
                            if len(matricula) > 1:                
                                print('matricula', matricula)
                                try:
                                    if matricula[1] in m :
                                        print('match')
                                        func()
                                        print('enviar html porta aberta')
                                        cl.send(response)
                                        cl.close()                        
                                    else:
                                        print ('sorry baby!' ,request.split(" ")[1])
                                        cl.send(response)
                                        cl.close()

                                except ValueError as err:
                                    print(err)
                        else:
                            print('nao "/" nem matricula enviar 404')
                            cl.send(response)
                            cl.close()
                    else:
                        print('msg request estranho')
                        cl.send(response)
                        cl.close()
                else:
                    print('nao get')
                    cl.close()
        #except:
        #    pass

    def tratamentoGet(self,msg):
        try:
            msg_req = ''
            method = ''
            msg = str(msg).split(' ')

            if msg[0].find('GET') > 0:
                msg_req = msg[1]
                method = 'GET'
            elif msg[0] == "POST":
                method = 'POST'
            else:
                method = 'unknow'

            return method , msg_req
        except:
            return False, False


