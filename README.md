# IoT Honeypot Monitoring System

## Overview

This project is a **low-interaction IoT honeypot** designed to simulate vulnerable services and capture malicious activity.
It helps in understanding attacker behavior, logging intrusion attempts, and analyzing common attack patterns on IoT devices.

---

## Features

* Simulated services:

  * HTTP Honeypot
  * Telnet Honeypot
* Packet sniffing for network traffic monitoring
* Attack logging and storage using SQLite database
* Dashboard for viewing captured attacks
* Detection module for identifying suspicious activity

---

## Tech Stack

* Python
* Flask (for dashboard & templates)
* SQLite (database)
* Networking libraries (socket, scapy, etc.)

---

## Project Structure

```
.
├── index.html           # HTML templates (Flask)
├── dashboard.py          # Web dashboard
├── database.py           # Database handling
├── detector.py           # Attack detection logic
├── honeypot_http.py      # HTTP honeypot
├── honeypot_telnet.py    # Telnet honeypot
├── packet_sniffer.py     # Network traffic capture
├── honeypot.db           # SQLite database
└── README.md
```

---

## How It Works

* Fake services are exposed to attract attackers
* Incoming connections are logged
* Packets are captured and analyzed
* Suspicious activities are stored in the database
* Dashboard displays logs and insights

---

## Installation

```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
```

---

## Usage

Run the honeypot modules:

```
python honeypot_http.py
python honeypot_telnet.py
python packet_sniffer.py
```

Run the dashboard:

```
python dashboard.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## Important Note

This project **cannot run on GitHub Pages** because it requires a Python backend.
To deploy it online, use:

* Render
* Railway
* PythonAnywhere

---

## Use Cases

* Cybersecurity learning
* Attack pattern analysis
* IoT security research
* Network monitoring practice

---

## Future Improvements

* Add SSH honeypot
* Real-time alert system
* Advanced analytics dashboard
* Integration with threat intelligence APIs

---

## Disclaimer

This project is for **educational and research purposes only**.
Do not deploy on public networks without proper security measures.
