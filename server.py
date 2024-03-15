import socket
import pyautogui
import pickle
import zlib

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 55000))  # Bind to all available network interfaces
    server_socket.listen(1)

    # Print the current IP address of the host
    hostname = socket.gethostname()    
    ip_address = socket.gethostbyname(hostname)
    print("Server started. IP address:", ip_address)

    print("Server started. Waiting for connection...")

    conn, addr = server_socket.accept()
    print("Connection established with", addr)

    try:
        while True:
            # Capture the screen content
            screenshot = pyautogui.screenshot()
            
            # Compress the screenshot data
            compressed_data = zlib.compress(pickle.dumps(screenshot))
            
            # Send the compressed data to the client
            conn.sendall(compressed_data)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
