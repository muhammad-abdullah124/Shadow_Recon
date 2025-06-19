# 🕶️ Shadow Recon — Stealthy Reconnaissance Toolkit for Red Teams

**Shadow Recon** is a lightweight yet powerful reconnaissance tool developed during an Offensive Security internship at ITSOLERA. Built with modularity and real-world red teaming in mind, it automates passive and active information gathering phases used in modern penetration testing.

---

## 🚀 Features

- 🔍 WHOIS Lookup  
- 🌐 DNS Record Enumeration (A, MX, TXT, NS)  
- 🔎 Subdomain Enumeration via crt.sh  
- 🔐 Port Scanning (Full range 1–1024 TCP)  
- 🛰️ Banner Grabbing  
- 📍 IP Address Resolution  
- 🧠 Technology Detection (Offline Wappalyzer)  
- 📄 Clean `.txt` Report Generation  
- 🛠️ Modular CLI Options with Logging

---

## 🛠️ System Requirements

- Python 3.8+
- OS: Linux or Windows (tested on linux)
- Dependencies: Listed in `requirements.txt`

---

## 📦 Installation

```bash

# Clone the repository
git clone https://github.com/muhammad-abdullah124/Shadow_Recon.git

# Change directory
cd Shadow_Recon

```

---

## 🧰 Setting Up a Virtual Environment (Recommended)

To avoid dependency conflicts, it is recommended to create and use a Python virtual environment.

```bash
# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # For Linux/macOS

# For Windows (PowerShell)
# .\\venv\\Scripts\\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

## ⚙️ Usage

Run the tool from the terminal using Python:

```bash
python3 main.py --domain example.com --whois --dns --subdomains --ports --banner --ip
```
---

### 🧾 Command-Line Flags

| Flag                | Description                                                                 | Example                                              |
|---------------------|-----------------------------------------------------------------------------|------------------------------------------------------|
| `--domain`          | **(Required)** Target domain name                                           | `--domain example.com`                               |
| `--whois`           | Perform WHOIS lookup on the domain                                          | `--domain example.com --whois`                       |
| `--dns`             | Enumerate DNS records (A, MX, TXT, NS)                                      | `--domain example.com --dns`                         |
| `--subdomains`      | Enumerate subdomains using crt.sh                                           | `--domain example.com --subdomains`                  |
| `--port`            | Scan open TCP ports (1–1024)                                                | `--domain example.com --ports`                       |
| `--banner`          | Perform banner grabbing on open ports                                       | `--domain example.com --banner`                      |
| `--ip`              | Resolve and display the IP address of the domain                            | `--domain example.com --ip`                          | 
