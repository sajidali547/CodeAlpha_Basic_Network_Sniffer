from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime
import csv
import os

csv_file = "captured_packets.csv"

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp", "Source IP", "Destination IP",
            "Protocol", "Source Port", "Destination Port", "Length"
        ])

def analyze_packet(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if IP not in packet:
        return

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    length = len(packet)

    protocol = "OTHER"
    src_port = "-"
    dst_port = "-"

    if TCP in packet:
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif UDP in packet:
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
    elif ICMP in packet:
        protocol = "ICMP"

    print("=" * 75)
    print(f"Time        : {timestamp}")
    print(f"Source IP   : {src_ip}")
    print(f"Destination : {dst_ip}")
    print(f"Protocol    : {protocol}")
    print(f"Source Port : {src_port}")
    print(f"Dest Port   : {dst_port}")
    print(f"Length      : {length} bytes")

    if Raw in packet:
        payload = bytes(packet[Raw].load[:80])
        print(f"Payload     : {repr(payload)}")

    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            timestamp, src_ip, dst_ip,
            protocol, src_port, dst_port, length
        ])

print("[+] Network Sniffer Started")
print("[+] Press CTRL+C to stop\n")

sniff(iface="ens34", prn=analyze_packet, store=False)
