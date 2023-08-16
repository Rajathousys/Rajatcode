import serial
import requests

ser = serial.Serial('/dev/serial0', baudrate=115200, timeout=1)

SERVER_URL = 'http://your-server-url.com/api/qrcode'
GATE_STATUS_URL = 'http://your-server-url.com/api/gate_status'  # URL for sending/receiving gate status

def read_qr_code():
    ser.write(b'READ_QR\r\n')
    response = ser.readline()
    return response.decode('utf-8').strip()

def send_to_server(qr_code):
    data = {'qr_code': qr_code}
    try:
        response = requests.post(SERVER_URL, json=data)
        response.raise_for_status()
        print("Data sent to server successfully")
    except requests.exceptions.RequestException as e:
        print("Error sending data to server:", e)

def get_gate_status():
    try:
        response = requests.get(GATE_STATUS_URL)
        response.raise_for_status()
        return response.json().get('command')
    except requests.exceptions.RequestException as e:
        print("Error getting gate status:", e)
        return None

def main():
    try:
        while True:
            qr_code = read_qr_code()
            if qr_code:
                print("QR Code:", qr_code)
                send_to_server(qr_code)

                gate_command = get_gate_status()
                if gate_command == "ON":
                    print("Opening Entry Gate")
                    # Add your code here to open the entry gate

                elif gate_command == "OFF":
                    print("Opening Exit Gate")
                    # Add your code here to open the exit gate

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()
