import machine
import socket
import uselect
from machine import Pin
from time import sleep
MATRICULAS = []
botao = Pin(12, Pin.IN,Pin.PULL_UP)
rele = Pin(15,Pin.OUT)
led_verde = Pin(13,Pin.OUT)
led_red = Pin(16,Pin.OUT)
#função que libera a porta
def porta_abrir(status):
    try:
        rele.value(status)
        led_red.value(not(status))    
    except :
        print('porta abrir')
#função que libera porta pelo botao
def botao_abrir():
    try:
        if botao.value():
            porta_abrir(0)        
        else:
            porta_abrir(1)        
    except :
        print('nop')
        pass

html = b'HTTP/1.0 200 OK\r\n Content-Type:text/html; charset=UTF-8\r\n\r\n'+"""<!DOCTYPE html>
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
addr = socket.getaddrinfo('0.0.0.0', 8012)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
poller = uselect.poll()
poller.register(s, uselect.POLLIN)
s.bind(addr)
s.listen(1)
print('listening on', addr)
while True:
    botao_abrir()
    print('in loop')
    res = poller.poll(300)
    if not res:
        print('not rcv')
    else:
        cl, addr = s.accept()
        request = cl.recv(1023)        
        response = html+'\n'
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
                print('abriu')
                porta_abrir(1)
                sleep(3)
            else:
                print ('sorry baby!' ,request.split(" ")[0])
                porta_abrir(0)
        else:
            print('iji')
            pass


# Teste do RFID
# from rfidPorteiro import RfidPorteiro
# rf = RfidPorteiro()
# tags = ["521252194","212516444","211595197"]
# while(True):
#     rf.get(tags)
#     print(rf.get(tags))