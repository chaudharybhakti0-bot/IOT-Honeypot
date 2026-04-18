import sqlite3

conn = sqlite3.connect("honeypot.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS telnet_commands(
id INTEGER PRIMARY KEY AUTOINCREMENT,
ip TEXT,
command TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS connections(
id INTEGER PRIMARY KEY AUTOINCREMENT,
ip TEXT,
port INTEGER,
flags TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS alerts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
type TEXT,
ip TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS auth_attempts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT,
password TEXT,
ip TEXT,
time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database created successfully")