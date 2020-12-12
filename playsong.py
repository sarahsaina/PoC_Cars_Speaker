#import libraries

import serial
import pygame
import datetime

pygame.init()   #initializes all modules
pygame.mixer.init()   #initializes the mixer module

ser = serial.Serial('/dev/ttyUSB0', 9600)
date = datetime.datetime.now()    #get the current date
print(date)

#create playlists
playlist1 = list()
playlist1.append('/home/pi/musique/playlist1/Lgbiri.mp3')   #path to sound file
playlist1.append('/home/pi/musique/playlist1/party1.mp3')
playlist1.append('/home/pi/musique/playlist1/party2.mp3')

playlist2 = list()
playlist2.append('/home/pi/musique/playlist2/6lack1.mp3')
playlist2.append('/home/pi/musique/playlist2/6lack2.mp3')

playlist3 = list()
playlist3.append('/home/pi/musique/playlist3/Rema1.mp3')
playlist3.append('/home/pi/musique/playlist3/Rema2.mp3')

playlist4 = list()
playlist4.append('/home/pi/musique/playlist4/JokeDC.mp3')
playlist4.append('/home/pi/musique/playlist4/Home.mp3')

while True:   #infinite loop
        if(ser.in_waiting > 0):
                totale = ser.readline()   #get the value sent by the esp32
                #separate the 2 values to recover the temp and the luminosity
                tab = totale.split (',')
          
                lumi = tab[1]   #brightness is the second value
                lumi = float(lumi)
                print('brightness : ')
                print(lumi)
                temp = tab[0]   #temperature is the first value
                temp = float(temp)
                print('temperature :')
                print(temp)
                if (date.hour > 22):    #date.hour return the current time
                        print("Evening playlist (after 10 p.m.)")
                        pygame.mixer.music.load(playlist1.pop())  #get the first track from the playlist
                        pygame.mixer.music.queue(playlist1.pop())    #queue the 2nd song
                        pygame.mixer.music.queue(playlist1.pop())    #queue the 3rd song
                        pygame.mixer.music.set_endevent(pygame.USEREVENT)  #setup the end track even
                        pygame.mixer.music.play()  #play the music
                        
                elif (lumi<100 and temp<15 ):  
                        print("Winter playlist (brightness<100 & temperature<15)")
                        pygame.mixer.music.load(playlist2.pop())
                        pygame.mixer.music.queue(playlist2.pop())
                        pygame.mixer.music.set_endevent(pygame.USEREVENT)
                        pygame.mixer.music.play()      
                        
                elif (lumi>100 and temp>15):    
                        print("Summer playlist (brightness>100 & temperature>15)")
                        pygame.mixer.music.load(playlist3.pop())
                        pygame.mixer.music.queue(playlist3.pop())
                        pygame.mixer.music.set_endevent(pygame.USEREVENT)
                        pygame.mixer.music.play()
                        
                else: #playlist 4
                        print("Playlist Regular")
                        pygame.mixer.music.load(playlist4.pop())
                        pygame.mixer.music.queue(playlist4.pop())
                        pygame.mixer.music.set_endevent(pygame.USEREVENT)
                        pygame.mixer.music.play()
                        
                for event in pygame.event.get():
                        if event.type == pygame.USEREVENT:    # A track has ended
                                if (len(playlist1) > 0 or len(playlist2) > 0 or len(playlist3) > 0 or len(playlist4) > 0):     # If there are more tracks in the queue...
                                         pygame.mixer.music.queue ( playlist.pop() )   #queue a sound file to follow the current 
