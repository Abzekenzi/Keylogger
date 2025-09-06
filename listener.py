import socket

BUFFER_SIZE = 10

import logging

def log_bytearray_to_file(buffer: bytearray, filename: str):
    if not isinstance(buffer, bytearray):
        raise TypeError("buffer must be a bytearray")

    with open(filename, "ab") as f:  # append in binary mode
        f.write(buffer.replace(b"\n", b" ") + b"\n")

def beautify_log(filename):
    file = open(filename, 'r')


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    buffer = ""
    output_file = open("log.txt", 'a', encoding="utf-8")

    host = '127.0.0.1'
    port = 4444

    server_socket.bind((host, port))
    server_socket.listen()

    conn, addr = server_socket.accept()
    
    while True:
        if len(buffer) <= BUFFER_SIZE:
            data = conn.recv(1)
            if data:
                buffer += data.decode("utf-8")
            else:
                print("No data has been received")
                beautify_log("log.txt")
                break
        else:
            print(buffer)
            output_file.write(buffer.replace("'", ""))
            buffer = ""
    output_file.close()


if __name__ == "__main__":
    main()
