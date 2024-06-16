from scapy.all import sniff, Ether, IP, TCP, UDP

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        print(f"IP Packet: {src_ip} -> {dst_ip} [Protocol: {protocol}]")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"TCP Segment: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            if packet.haslayer("Raw"):
                print(f"Raw Data: {packet[Raw].load}")
        
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"UDP Datagram: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
            if packet.haslayer("Raw"):
                print(f"Raw Data: {packet[Raw].load}")

def main():
    print("Network Packet Analyzer - Press Ctrl+C to stop sniffing")
    try:
        sniff(prn=packet_handler, count=10)  # Adjust count as needed
    except KeyboardInterrupt:
        print("Sniffing stopped.")

if __name__ == "__main__":
    main()
