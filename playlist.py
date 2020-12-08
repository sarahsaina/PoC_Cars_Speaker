import serial
import pygame
import datetime
import os
import sys, getopt
import time

lumiref = int(sys.argv[1]) #brightness converted in int
#print(lumiref)
tempref = int(sys.argv[2]) #temperature converted in it
#print(tempref)
ser = serial.Serial('/dev/ttyUSB0', 9600)
date = datetime.datetime.now()    #get the current date


while True:     #infinite loop
        if(ser.in_waiting > 0):
                totale = ser.readline()
        #separate the 2 values to recover the temperature and the brightness
                tab = totale.split (',')
                #print(tab)
                lumi = tab[1]   #brightness is the second value
                lumi = float(lumi)
                print('luminosite : ')
                print(lumi)
                temp = tab[0]   #temperature is the first value
                temp = float(temp)
                print('temperature :')
                print(temp)
                
                if (date.hour > 22):    #date.hour return the current time
                        os.system('omxplayer /home/pi/musique/playlist1/party1.mp3')
                        time.sleep(15)    #suspend the execution for 15 seconds
                        os.system('sudo killall "omxplayer.bin"')
                elif (lumi>lumiref and temp>tempref ):
                        os.system('omxplayer /home/pi/musique/playlist3/Rema1.mp3')
                        time.sleep(15)
                        os.system('sudo killall "omxplayer.bin"')
                elif (lumi<lumiref and temp<tempref):
                        os.system('omxplayer /home/pi/musique/playlist2/6lack1.mp3')
                        time.sleep(15)
                        os.system('sudo killall "omxplayer.bin"')
                else :
                        os.system('omxplayer /home/pi/musique/playlist4/Home.mp3')
                        time.sleep(15)
                        os.system('sudo killall "omxplayer.bin"')

