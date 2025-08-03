import socket

BUFFER_SIZE = 10

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buffer = bytearray()

    host = '127.0.0.1'
    port = 4444

    server_socket.bind((host, port))
    server_socket.listen()

    conn, addr = server_socket.accept()
    
    while True:
        if len(buffer) <= BUFFER_SIZE:
            data = conn.recv(1)
            if data:
                buffer.extend(data)
            else:
                print("No data has been received")
        else:
            print(buffer.decode().replace("''", ""))
            buffer.clear()



if __name__ == "__main__":
    main()
