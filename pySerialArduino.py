#!/usr/bin/python

import serial,shlex,time
import sys
import re

arduinoData = serial.Serial('/dev/ttyACM0',9600)
arduinoData.flushInput()

def ledON():
    arduinoData.write('0')

def ledOFF():
    arduinoData.write('1')

if __name__=="__main__":

    loopFlag = True

    time.sleep(5)

    count = 0
    while(loopFlag == True):
        """
        cmdLine = raw_input('Enter command [read|write]: ')
        if not cmdLine:
            continue
        usrInput = shlex.split(cmdLine)
        
        if usrInput[0] == 'read':
            arduino_bytes = arduinoData.readline()
            decoded_bytes = float(arduino_bytes[0:len(arduino_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
            while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
    except:
        print("Keyboard Interrupt")
        break

        """
        arduino_bytes = arduinoData.readline()
        #print arduino_bytes
        #print
        print arduino_bytes.decode("utf-8")
        #decoded_bytes = float(arduino_bytes[0:len(arduino_bytes)-2].decode("utf-8"))
        #print(decoded_bytes)
        speed_value=''
        temp_value=''
        speed_pattern=re.compile('(Speed\s\(\%\sduty\scicle\):)(.*)') 
        temp_pattern=re.compile('(Temperature:\s)([0-9\.]+)')
        regexp_result=speed_pattern.search(arduino_bytes.decode('utf-8'))
        if regexp_result:
            speed_label=regexp_result.group(1).strip(' ')
            speed_value=regexp_result.group(2)
        regexp_temp=temp_pattern.search(arduino_bytes.decode('utf-8'))
        if regexp_temp:
            temp_label=regexp_temp.group(1)
            temp_value=regexp_temp.group(2).strip(' ')
        count = count +1
        if (count > 500):
            if speed_value:
                print ('speed_value: '  + speed_value )
            if temp_value:
                print ('temp_value: ' + temp_value )
            count = 0
