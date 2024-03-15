import socket
import pickle
import zlib
from PIL import Image
import io

def main():
    server_ip = input("Enter server IP: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 55000))

    try:
        while True:
            # Receive compressed screenshot data from the server
            compressed_data = client_socket.recv(4096)
            
            # Decompress the data
            screenshot_data = zlib.decompress(compressed_data)
            
            # Deserialize the data
            screenshot = pickle.loads(screenshot_data)
            
            # Display the screenshot
            screenshot.show()
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
