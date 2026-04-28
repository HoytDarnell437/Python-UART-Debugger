import serial

# open serial port
ser = serial.Serial('/dev/cu.usbserial-20250303171', 9600)
print(ser.read())