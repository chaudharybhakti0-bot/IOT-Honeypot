from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/")
def login_page():
    return """
    <h2>IoT Camera Login</h2>
    <form method="POST" action="/login">
    Username:<br>
    <input name="username"><br><br>
    Password:<br>
    <input name="password" type="password"><br><br>
    <button type="submit">Login</button>
    </form>
    """

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username")
    password = request.form.get("password")
    ip = request.remote_addr

    conn = sqlite3.connect("honeypot.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO auth_attempts(username,password,ip) VALUES(?,?,?)",
        (username,password,ip)
    )

    conn.commit()
    conn.close()

    return "Login Failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)