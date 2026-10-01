# Packet Analysis Report

## 1. ICMP Analysis

- Generated using `ping` from Windows to Ubuntu
- Python sniffer identified protocol as ICMP
- Wireshark filter: `icmp`
- Observed Echo Request and Echo Reply packets

## 2. HTTP Analysis

- Generated using `curl.exe` from Windows to Ubuntu HTTP server on port 8000
- Python sniffer identified TCP with destination port 8000
- Wireshark filter: `http`
- Inspected GET request, Host header, and User-Agent

## 3. DNS Analysis

- Generated using `nslookup google.com` from Windows
- Python sniffer identified UDP traffic (port 53)
- Wireshark filter: `dns`
- Inspected DNS query for google.com

## 4. Python Scapy vs Wireshark

| Python Scapy Sniffer | Wireshark |
|---|---|
| Programmatic capture | GUI packet analysis |
| Displays selected fields | Full packet dissection |
| Can automate analysis | Excellent manual investigation |
| Easy to customize | Hundreds of protocol decoders |
| Useful for scripting | Useful for deep packet inspection |

## Conclusion

The Python Scapy sniffer provided programmatic visibility into network traffic, while Wireshark offered detailed packet-level validation. Combining both tools demonstrates a practical network monitoring workflow used in SOC environments.
