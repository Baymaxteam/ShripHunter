# FreqAddr 		2000H = 8192		
# ControlAddr 	2001H = 8193

# Stop 			000001 – 0x01
# FWD direction	010010  - 0x12 - 18
# REV direction	100010  - 0x22 - 34
# Change			110010 - 0x32 - 50
# minimalmodbus - https://minimalmodbus.readthedocs.io/en/master/installation.html

#!/usr/bin/env python
import minimalmodbus
import serial
from time import sleep
import sys

# modbus address
MotorFreqAddr = 8193
MotorControlAddr = 8192

# control value
MotorSTOP = 1
MotorFWD = 18
MotorREV = 34

# Motor Control variable
CommendSTOP = 0
CommendFWD = 1
CommendREV = -1
# MotorFreq variable
CommendMotorFreq = 1500

def writeMotionFreq(DeviceID, value):
	# avoid to large freq
	if (value > 6000):
		value = 6000
	if (value < -6000):
		value = -6000	

	if (value > 0):
		DeviceID.write_register(MotorFreqAddr, value, 0, 6)
		writeMotionControl(DeviceID, CommendFWD)
	else:
		DeviceID.write_register(MotorFreqAddr, -value, 0, 6)
		writeMotionControl(DeviceID, CommendFWD)

def writeMotionControl(DeviceID, value):
	if(value == 1):
		DeviceID.write_register(MotorControlAddr, MotorFWD, 0, 6)
	elif (value == -1):
		DeviceID.write_register(MotorControlAddr, MotorREV, 0, 6)
	else:
		DeviceID.write_register(MotorControlAddr, MotorSTOP, 0, 6)

def StopMotor():
	instrument1.write_register(MotorControlAddr, MotorSTOP, 0, 6)
	sleep(0.1) # Time in seconds.
	instrument2.write_register(MotorControlAddr, MotorSTOP, 0, 6)
	sleep(0.1) # Time in seconds.
	instrument3.write_register(MotorControlAddr, MotorSTOP, 0, 6)
	sleep(0.1) # Time in seconds.

def writeAllMotionFreq(value1, value2, value3):
	writeMotionFreq(instrument1, value1)
	sleep(0.1) # Time in seconds.
	writeMotionFreq(instrument2, value2)
	sleep(0.1) # Time in seconds.
	writeMotionFreq(instrument3, value3)
	sleep(0.1) # Time in seconds.


########### init Modbus/RTU functon ###############
instrument1 = minimalmodbus.Instrument('COM8',1) # port name (in decimal)
instrument1.serial.baudrate = 9600   # Baud
instrument1.serial.bytesize = 8
instrument1.serial.parity   = serial.PARITY_NONE
instrument1.serial.stopbits = 2
instrument1.serial.timeout  = 1   # seconds
instrument1.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode

instrument2 = minimalmodbus.Instrument('COM8',2) # port name (in decimal)
instrument2.serial.baudrate = 9600   # Baud
instrument2.serial.bytesize = 8
instrument2.serial.parity   = serial.PARITY_NONE
instrument2.serial.stopbits = 2
instrument2.serial.timeout  = 1   # seconds
instrument2.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode

instrument3 = minimalmodbus.Instrument('COM8',3) # port name (in decimal)
instrument3.serial.baudrate = 9600   # Baud
instrument3.serial.bytesize = 8
instrument3.serial.parity   = serial.PARITY_NONE
instrument3.serial.stopbits = 2
instrument3.serial.timeout  = 1   # seconds
instrument3.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode

############### main function #############


writeAllMotionFreq() # control motor
sleep(1) # Time in seconds.
StopMotor() # stop all motor
sleep(1) # Time in seconds.


# writeMotionFreq(instrument1, CommendMotorFreq)

# writeMotionControl(instrument1, CommendFWD)
# writeMotionControl(instrument1, CommendREV)
# writeMotionControl(instrument1, CommendSTOP)


# writeAllMotionFreq(CommendMotorFreq,CommendMotorFreq,CommendMotorFreq)
# writeMotionControl(instrument1, CommendFWD)
# sleep(1) # Time in seconds.
# StopMotor() # stop all motor

################### End #####################