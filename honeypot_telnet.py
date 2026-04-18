import socket
import sqlite3

HOST = "0.0.0.0"
PORT = 2323

server = socket.socket()
server.bind((HOST, PORT))
server.listen(5)

print("Telnet honeypot running on port 2323")

while True:

    client, addr = server.accept()
    ip = addr[0]

    client.send(b"login: ")
    username = client.recv(1024).decode().strip()

    client.send(b"password: ")
    password = client.recv(1024).decode().strip()

    conn = sqlite3.connect("honeypot.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO auth_attempts(username,password,ip) VALUES(?,?,?)",
        (username, password, ip)
    )

    conn.commit()

    client.send(b"\nWelcome to IoT device\n")

    while True:

        client.send(b"# ")
        cmd = client.recv(1024).decode().strip()

        cur.execute(
            "INSERT INTO telnet_commands(ip,command) VALUES(?,?)",
            (ip, cmd)
        )

        conn.commit()

        client.send(b"command not found\n")