from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():

    conn = sqlite3.connect("honeypot.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM auth_attempts ORDER BY id DESC")
    rows = cur.fetchall()

    conn.close()

    return render_template("index.html", rows=rows)


if __name__ == "__main__":
    app.run(port=9000)