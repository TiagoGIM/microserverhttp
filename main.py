from rfidPorteiro import RfidPorteiro
import urequests
from uconnect import uConnect 
import time
cn = uConnect()
cn.wlan_manual()

rf = RfidPorteiro()
tags = ["521252194","212516444","211595197"]
while(True):

    tag = str(rf.get())
    time.sleep_ms(100)
    if tag != "SemTag":
        print(tag)
        print ("okok")
        url = "http://10.6.3.114:8012/?Matricula="+tag
        response = urequests.get(url)
