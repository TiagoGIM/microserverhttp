from rfidPorteiro import RfidPorteiro
import urequests
from uconnect import uConnect 
import time
cn = uConnect()
cn.wlan_manual()
rf = RfidPorteiro()

while(True):

    tag = str(rf.get())
    time.sleep_ms(100)

    if tag != "SemTag":
        print(tag)
        print ("okok")
        url = "http://10.6.3.114:8012/?Matricula="+tag
        #url = "http://10.6.3.114:8012/?Tag="+tag
        response = urequests.get(url)
