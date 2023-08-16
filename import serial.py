import serial

# Configure the serial port with the appropriate UART pins and settings
ser = serial.Serial('/dev/ttyS0', baudrate=115200, timeout=1)  # Use /dev/ttyS0 for UART pins GPIO14 and GPIO15

def read_qr_code():
    ser.write(b'READ_QR\r\n')  # Send command to read QR code
    response = ser.readline()  # Read response from scanner
    return response.decode('latin-1').strip()

def main():
    try:
        while True:
            qr_code = read_qr_code()
            if qr_code:
                print("QR Code:", qr_code)
    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()



    
