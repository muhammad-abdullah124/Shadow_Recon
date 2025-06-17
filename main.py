import argparse
import whois
import dns.resolver
import requests
import socket
import datetime
import logging

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# WHOIS Lookup

def whois_lookup(domain):
    try:
        logging.info("Running WHOIS Lookup")
        w = whois.whois(domain)
        return w.text
    except Exception as e:
        logging.error(f"WHOIS error: {e}")
        return "WHOIS lookup failed"

# DNS Records

def dns_records(domain):
    records = {}
    for record_type in ['A', 'MX', 'TXT', 'NS']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            records[record_type] = [rdata.to_text() for rdata in answers]
        except:
            records[record_type] = []
    return records

# Subdomain Enumeration using crt.sh

def subdomain_enum(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        logging.info("Running Subdomain Enumeration")
        r = requests.get(url, timeout=10)
        data = r.json()
        subdomains = set()
        for entry in data:
            name_value = entry['name_value']
            for sub in name_value.split('\n'):
                subdomains.add(sub)
        return list(subdomains)
    except Exception as e:
        logging.error(f"Subdomain enumeration error: {e}")
        return []

# Port Scanning

def port_scan(domain):
    open_ports = []
    ports = range(1, 100)
    logging.info("Running Port Scan")
    for port in ports:
        try:
            s = socket.create_connection((domain, port), timeout=2)
            open_ports.append(port)
            s.close()
        except:
            continue
    return open_ports

# Banner Grabbing

def banner_grab(domain, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((domain, port))
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = s.recv(1024).decode(errors='ignore')
        s.close()
        return banner
    except:
        return "No banner"

# IP Resolution
def resolve_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except:
        return "Could not resolve IP"

# Report Generator

def generate_report(domain, data):
    filename = f"{domain}_report.txt"
    with open(filename, "w") as f:
        f.write(f"Report for {domain}\n")
        f.write(f"Generated on: {datetime.datetime.now()}\n\n")
        for section, content in data.items():
            f.write(f"--- {section} ---\n")
            if isinstance(content, dict):
                for key, value in content.items():
                    f.write(f"{key}: {value}\n")
            elif isinstance(content, list):
                for item in content:
                    f.write(f"{item}\n")
            else:
                f.write(f"{content}\n")
            f.write("\n")
    logging.info(f"Report generated: {filename}")

# Argument Parser

def main():
    parser = argparse.ArgumentParser(description='Custom Recon Tool')
    parser.add_argument('--domain', required=True, help='Target domain')
    parser.add_argument('--whois', action='store_true', help='Perform WHOIS lookup')
    parser.add_argument('--dns', action='store_true', help='Perform DNS enumeration')
    parser.add_argument('--subdomains', action='store_true', help='Perform Subdomain enumeration')
    parser.add_argument('--ports', action='store_true', help='Perform Port scanning')
    parser.add_argument('--banner', action='store_true', help='Perform Banner grabbing')
    parser.add_argument('--ip', action='store_true', help='Resolve domain to IP address')
    
    args = parser.parse_args()
    domain = args.domain
    data = {}

    if args.ip:
        data['IP Resolution'] = resolve_ip(domain)
    if args.whois:
        data['WHOIS'] = whois_lookup(domain)
    if args.dns:
        data['DNS Records'] = dns_records(domain)
    if args.subdomains:
        data['Subdomains'] = subdomain_enum(domain)
    if args.ports:
        ports = port_scan(domain)
        data['Open Ports'] = ports
        if args.banner:
            banners = {}
            for port in ports:
                banners[port] = banner_grab(domain, port)
            data['Banners'] = banners

    generate_report(domain, data)

if __name__ == '__main__':
    main()
