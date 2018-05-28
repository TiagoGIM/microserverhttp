import socket 
import uselect

#addr = socket.getaddrinfo('0.0.0.0', 8012)[0][-1]
#s = socket.socket()
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# s.bind(addr)
# s.listen(1)

class BotaoWeb:
    kind = 'Classe do botao virtual'

    def __init__(self, port, host):
        self.port = port
        self.host = host
        self.poller = uselect.poll()

        self.msgWeb = b'HTTP/1.0 200 OK\r\n Content-Type:text/html; charset=UTF-8\r\n\r\n'+"""<!DOCTYPE html>
            <html>
                <head> <title>PORTA LAR</title> </head>
                <body> <h1>Em testes</h1>
                    <form action="/">
                        Matricula: <input type="text" name="Matricula" value="12345"><br>
                        <input type="submit" value="Submit">
                    </form>
                    <footer><p> by: Tiago Herique </p></footer>
                </body>
            </html>
            """

    def setConnection(self):
        self.addr = socket.getaddrinfo(self.port, self.host)[0][-1]
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.poller.register(self.s, uselect.POLLIN)
        self.s.bind(self.addr)
        self.s.listen(1)
        print('listening on', self.addr)


    def botaoWeb(self,func, MATRICULAS):
        res = self.poller.poll(30)
        if not res:
            pass
        else:
            cl, addr = self.s.accept()
            request = cl.recv(1023)        
            response = self.msgWeb+'\n'
            cl.send(response)
            cl.close()

            request = str(request).split('/')[1]
            print(request)
            request = request.split(" ")[0]
            print('new request')
            matricula = request.split("=")

            if len(matricula) > 1:
                print('matricula', matricula) 
                if matricula[1] in MATRICULAS :
                    func()                        
                else:
                    print ('sorry baby!' ,request.split(" ")[0])
            else:
                print('iji')
                pass
        


