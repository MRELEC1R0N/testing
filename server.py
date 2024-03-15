import socket

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind(('0.0.0.0', 9999))
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    # Get the server's IP address
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    print("Server IP address:", server_ip)
    
    print("Server started. Waiting for connection...")
    
    # Accept a client connection
    conn, addr = server_socket.accept()
    print("Connection established with:", addr)
    
    # Send a message to the client
    conn.sendall("Connection successful. Welcome to the server!".encode())
    
    # Close the connection
    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()
