import socket 
import uselect
import network
from classes.db import Datapages
from time import sleep


class BotaoWeb(Datapages):
    kind = 'Classe do botao virtual'

    def __init__(self, port, host,wf_configs):
        #wifi settings
        print('setuping wifi...')
        self.rede = wf_configs['ssid']
        self.senha = wf_configs['pw']
        self.w = network.WLAN(network.STA_IF)
        self.w.active(True)
        #socket config
        self.port = port
        self.host = host
        self.poller = uselect.poll()

        Datapages.__init__(self,'teste')
        self.openDB()
        self.msgWeb = self.openPage('home')
    
    def networkIp(self):        
        print(self.w.ifconfig())
        input('press keyboard for skip this method')

    def closeSock(self):
        self.s.close()  

    def setConnection(self):
        try:
            self.connect_wifi()#connecta na wifi   
            self.addr = socket.getaddrinfo(self.port, self.host)[0][-1]
            self.s = socket.socket()
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.poller.register(self.s, uselect.POLLIN)
            self.s.bind(self.addr)
            self.s.listen(1)
            print('listening on', self.addr)
            return True
        except:
            return False

    def botaoWeb(self,openDor,m):
        
            res = self.poller.poll(5)
            if not res:
                pass
            else:
                try:
                    cl, addr = self.s.accept()
                    request = cl.recv(1023)                
                    method , request = self.tratamentoGet(request)
                    if method == 'GET':
                        if request:
                            response = self.msgWeb+'\n'
                            if request =='/':
                                print('send response page home')                        
                                cl.send(response)
                            elif request.find("token")> 0:
                                token = request.split("=")
                                if len(token) > 1:                
                                    try:
                                        if token[1] in m :
                                            print('match')
                                            openDor()
                                            #send a msg ok!                    
                                        else:
                                            print ('sorry baby!')
                                            #send a msg denned!
                                    except :
                                        pass
                            elif request.find("Matricula") > 0:
                                matricula = request.split("=")
                                if len(matricula) > 1:                
                                    print('matricula', matricula)
                                    try:
                                        if matricula[1] in m :
                                            print('match')
                                            openDor()
                                            print('enviar html porta aberta')
                                            cl.send(response)
                                            # cl.close()                        
                                        else:
                                            print ('sorry baby!')
                                            cl.send(response)
                                            # cl.close()
                                    except :
                                        pass
                            elif request.find("cadastro") > 0:
                                try:
                                    print('sending cadastro page')
                                    cl.send(self.openPage('cadastro'))
                                except ValueError as err:
                                    print('fail', err)
                            else:
                                print('nao "/" nem matricula enviar 404')
                                # cl.send(response)
                        else:
                            print('msg request estranho')
                            # cl.send(response)
                        sleep(1)
                    else:
                        print('nao get')
                    cl.close()
                except:
                    pass

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

    def connect_wifi(self):
        self.w.connect(self.rede,self.senha)
        print('try connect in '+self.rede)
        #exibe status de conexão
        print(self.w.isconnected())
        #exibe ip
        print(self.w.ifconfig())
        #returna se foi connectado
        return self.w.isconnected()

    def reconnect(self):
        self.connect_wifi()
