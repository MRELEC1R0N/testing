# server.py
import socket
import pygetwindow as gw
import zlib
import pickle

def capture_screen():
    screenshot = gw.getActiveWindow().screenshot()
    return screenshot

def main():
    host = '127.0.0.1'  # Use your server's IP address
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        try:
            screenshot = capture_screen()
            compressed_screenshot = zlib.compress(pickle.dumps(screenshot))
            client_socket.sendall(compressed_screenshot)
        except KeyboardInterrupt:
            print("Server shutting down.")
            break

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
