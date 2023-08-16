import RPi.GPIO as GPIO
import serial

# Configure GPIO pins
GPIO.setmode(GPIO.BCM)
TXD_PIN = 27  # GPIO 0
RXD_PIN = 29  # GPIO 5
GPIO.setup(TXD_PIN, GPIO.OUT)
GPIO.setup(RXD_PIN, GPIO.IN)

# Create a UART object
ser = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

# Send and receive data
ser.write(b'READ_QR\r\n')







received_data = ser.readline()
print(received_data.decode('utf-8'))

# Cleanup GPIO
ser.close()
GPIO.cleanup()