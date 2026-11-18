from threading import Thread, Lock
import socket
from flask import Flask, request
from pathlib import Path

WORDS_FILE = Path("words.txt")
FILE_LOCK = Lock()
app = Flask(__name__)

def add_word_to_file(word: str):
    with FILE_LOCK:
        with open(WORDS_FILE, mode="a") as f:
            f.write(word.strip() + "\n")

@app.route("/words")
def get_wordlist():
    with FILE_LOCK:
        if not WORDS_FILE.is_file():
            return []
        with open(WORDS_FILE) as f:
            return [line.strip() for line in f]
            # lines = []
            # for line in f:
            #     lines.append(line.strip())
            # return lines

# @app.route("/words/<word>", methods=["POST"])
@app.route("/words", methods=["POST"])
def add_word():
    data = request.args.get("word", "")
    client = request.remote_addr
    # data = request.get_json()
    if data:
        print(f"WEBSERVER {client} => {data}")
        add_word_to_file(data)
        return "", 201
    return ""
    
def terminal_input():
    while True:
        data = input()
        print(f"TERMINAL => {data}")
        add_word_to_file(data)

def socket_input():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9000))
    server_socket.listen()
    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            client_socket.sendall(b"Welcome to the word server\n")
            data = client_socket.recv(1024)
            data = data.decode()
        print(f"SOCKET {client_address} => {data}")
        add_word_to_file(data)


t1 = Thread(target=terminal_input)
t2 = Thread(target=socket_input)
t1.start()
t2.start()
app.run("0.0.0.0", 9001)
