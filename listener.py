import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = '127.0.0.1'
    port = 4444

    server_socket.bind((host, port))
    server_socket.listen()

    conn, addr = server_socket.accept()
    try:
        while True:
            data = conn.recv(2048)
            if data:
                data_string = data.decode('utf-8')
                print(data_string)
            else:
                conn.close()
    except Exception as e:
        print("Error occured in data receiving: ", e)



if __name__ == "__main__":
    main()
