# Network Traffic Sniffer & Packet Analysis with Python Scapy and Wireshark

## CodeAlpha Cyber Security Internship - Task 1

## Overview

This project implements a Python-based packet sniffer using Scapy and validates captured network traffic using Wireshark.

The lab demonstrates packet capture and analysis across ICMP, TCP, HTTP, UDP, and DNS traffic in a controlled VMware environment.

## Lab Architecture

```text
Windows Test Endpoint
        |
        | ICMP / HTTP / DNS Traffic
        v
Ubuntu Server (ens34)
        |
        +--> Python Scapy Sniffer
        |
        +--> Wireshark
```

## Technologies Used

- Python 3
- Scapy
- Wireshark
- Ubuntu Linux
- Windows
- VMware

## Features

- Real-time packet capture using Scapy
- Protocol identification (TCP, UDP, ICMP)
- Source/Destination IP and port extraction
- Payload inspection
- CSV logging of captured packets
- Wireshark validation of the same traffic

## Files

- `sniffer.py` - Python packet sniffer
- `captured_packets.csv` - Sample captured packet log
- `screenshots/` - Project screenshots
- `docs/packet-analysis.md` - Detailed analysis

## How to Run

```bash
sudo python3 sniffer.py
```

## Skills Demonstrated

- Packet capture and analysis
- Python scripting for network security
- Scapy library usage
- Wireshark packet inspection
- ICMP/TCP/UDP/DNS protocol analysis
- Layer 2-7 traffic visibility
- Network traffic logging
- SOC-style traffic investigation

## Disclaimer

All traffic was generated in an isolated personal cybersecurity lab for educational purposes.
No unauthorized systems or networks were tested.
