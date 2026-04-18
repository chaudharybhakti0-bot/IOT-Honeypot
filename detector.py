import sqlite3
import time

print("Attack detector running...")

while True:

    conn = sqlite3.connect("honeypot.db")
    cur = conn.cursor()

    cur.execute("""
    SELECT ip, COUNT(*)
    FROM auth_attempts
    GROUP BY ip
    HAVING COUNT(*) > 5
    """)

    rows = cur.fetchall()

    for r in rows:

        ip = r[0]

        cur.execute(
        "INSERT INTO alerts(type,ip) VALUES(?,?)",
        ("Brute Force", ip)
        )

        print("ALERT: brute force from", ip)

    conn.commit()
    conn.close()

    time.sleep(20)