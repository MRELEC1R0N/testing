import socket

def main():
    # Prompt the user to enter the server's IP address
    server_ip = input("Enter server IP address: ")
    
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((server_ip, 9999))
    print("Connected to server.")
    
    # Receive message from server
    message = client_socket.recv(1024).decode()
    print("Message from server:", message)
    
    # Close the connection
    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
