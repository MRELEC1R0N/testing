# client.py
import socket
import zlib
import pickle
from PIL import Image

def main():
    host = '127.0.0.1'  # Use the server's IP address
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        try:
            compressed_screenshot = client_socket.recv(4096)
            screenshot = pickle.loads(zlib.decompress(compressed_screenshot))
            img = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())
            img.show()  # Display the received screen
        except KeyboardInterrupt:
            print("Client shutting down.")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
