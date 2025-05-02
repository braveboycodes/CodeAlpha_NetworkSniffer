from scapy.all import sniff  # Import sniff here

def packet_callback(packet):
    if packet.haslayer("IP"):  # Check if the packet has an IP layer
        ip_src = packet["IP"].src  # Extract source IP
        ip_dst = packet["IP"].dst  # Extract destination IP
        protocol = packet["IP"].proto  # Extract protocol type (TCP, UDP, etc.)
        
        # Print captured packet details
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol}")
        
        # Optionally, identify the type of protocol (TCP, UDP, ICMP)
        if packet.haslayer("TCP"):
            print("TCP Protocol detected.")
        elif packet.haslayer("UDP"):
            print("UDP Protocol detected.")
        elif packet.haslayer("ICMP"):
            print("ICMP Protocol detected.")

def start_sniffing():
    print("Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0, filter="ip", count=100)  # Indent this line to be part of the function

start_sniffing()
