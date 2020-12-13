# -*- coding: utf-8 -*-
import serial
from datetime import datetime
from time import sleep, strftime, time


ser = serial.Serial('/dev/ttyUSB0', 9600) #opens a serial port
# now will contain the current date and time
now = datetime.now()
# we create a csv file
with open('test8.csv','a') as data_file:
        while True: # infinite loop that will stop with CTRL+C
                if(ser.in_waiting > 0):
                        line = ser.readline()
                        list = line.split(',')
                        print(list)
                        # we want the date to be like YYYY/MM/DD
                        dt_string = strftime("%Y/%m/%d %H:%M:%S")
                        # we create a string that contains 3 placeholders separated by a ','
                        # the date and time are inserted in the first placeholder
                        # the temperature in the second one and the light in the third one
                        data_file.write("{0},{1},{2}\n".format(dt_string,list[0],list[1]))
                        sleep(1)
