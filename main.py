import socket
import uselect
from machine import Pin ,reset
from time import sleep, time
from os import listdir, remove


import network
w = network.WLAN(network.STA_IF)
w.active(True)
w.connect('','')

press = time()

time_to_reset = time()

status_porta = True

MATRICULAS = []


# seting ports for using                         
botao = Pin(12, Pin.IN,Pin.PULL_UP)
rele = Pin(15,Pin.OUT)
led_verde = Pin(13,Pin.OUT)
led_red = Pin(16,Pin.OUT)

#função que libera a porta
def door(status):
    """
    this method just chang the led's pins value and rele's pin.
    """
    try:
        rele.value(status)
        led_red.value(not(status))
        led_verde.value(status)    
    except :
        print('error in method door')

def porteiro(tempo):
    """
    this method compare which the last time the door() was
     used and wich is the status_porta for so att the status_porta
    """
    global press,status_porta
    elapsed = time() - press
    try:
        if elapsed > tempo and status_porta:
            door(0)
            status_porta = False
            print('fechar')
        elif elapsed < tempo and not status_porta:
            door(1)
            status_porta = True
            print('abrir')
        else:
            print('e ai?')

    except :
        print('error > porteiro')


def openDoor():
    press = time()
    print('press att')


#função que libera porta pelo botao
def pushButton():
    try:
        if not(botao.value()):
            openDoor()
        else:
            pass
    except :
        print('troble pushButton')
        pass

def manutencao():
    door(1)
    input('press keyboard for restart loop')
    main()



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

def main():

    global time_to_reset
    loop = True

    while loop:
        #reseta o esp para previnir bugs
        if (time() - time_to_reset > (15*60)):
            reset()
            time_to_reset = time()

        porteiro(2)
        pushButton()
        
        try:
            res = poller.poll(30)
            if not res:
                pass
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
                        openDoor()                        
                    else:
                        print ('sorry baby!' ,request.split(" ")[0])
                else:
                    print('iji')
                    pass
        except:
            x = input('enter comand [d = reset, x = exit loop, m = aberta permanente] >>')
            if x == 'd':
                reset()
            elif x == 'x':
                print('X')
                loop = False
            elif x == 'm':
                manutencao()
sleep(5)
main()