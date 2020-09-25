import serial
import time

##########################################
[查詢USB位置]
pi@nesspi:~$ls -i /dev/tty*
##########################################
ser = serial.Serial('/dev/ttyUSB1', 9600)  ## 9600是你的baud rate
ser.flushInput()

while True:
    bytearr = ser.readline()                #read Arduino println
    string = bytearr.decode()
    s = string.rstrip('\r\n')
    list = s.split(",")
    #pstr='{"sensor1":{"value":'+list[0]+'},"sensor1":{"value":'+list[1]+'}}'
    #print(pstr)
    sensor1 = eval(list[0])
    print(sensor1)
    sensor2 = eval(list[1])
    print(sensor2)
