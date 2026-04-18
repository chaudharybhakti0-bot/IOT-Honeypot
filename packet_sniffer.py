from scapy.all import sniff, IP, TCP
import sqlite3

def process(pkt):

    if pkt.haslayer(TCP):

        ip = pkt[IP].src
        port = pkt[TCP].dport
        flags = pkt[TCP].flags

        conn = sqlite3.connect("honeypot.db")
        cur = conn.cursor()

        cur.execute(
        "INSERT INTO connections(ip,port,flags) VALUES(?,?,?)",
        (ip, port, str(flags))
        )

        conn.commit()
        conn.close()


print("Packet sniffer running...")

sniff(filter="tcp", prn=process)