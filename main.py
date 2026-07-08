import socket

Host = input("Enter a Hostname or Ip address: ")

Ports = [ 20 , 21 , 22 , 23 , 25 , 53 , 80 , 110 , 143 , 443 ]

SuccessfulPorts = []
FailedPorts = []

for Port in Ports:
    print("You're Now Checking: ", Port)
    
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

    sock.settimeout(1)

    result = sock.connect_ex((Host,Port))
    if result == 0:
        SuccessfulPorts.append(Port)
    else:
        FailedPorts.append(Port)

print("Results: ")

for SuccessfulPort in SuccessfulPorts:
    if SuccessfulPort == 20:
        print(f"FTP {SuccessfulPort} is open")
    if SuccessfulPort == 21:
        print(f"FTP {SuccessfulPort} is open")
    if SuccessfulPort == 22:
        print(f"SSH {SuccessfulPort} is open")
    if SuccessfulPort == 23:
        print(f"Telnet {SuccessfulPort} is open")
    if SuccessfulPort == 25:
        print(f"SMTP {SuccessfulPort} is open")
    if SuccessfulPort == 53:
        print(f"DNS {SuccessfulPort} is open")
    if SuccessfulPort == 80:
        print(f"HTTP {SuccessfulPort} is open")
    if SuccessfulPort == 110:
        print(f"POP3 {SuccessfulPort} is open")
    if SuccessfulPort == 143:
        print(f"IMAP {SuccessfulPort} is open")
    if SuccessfulPort == 443:
        print(f"HTTPS {SuccessfulPort} is open")
    
    

for FailedPort in FailedPorts:
    if FailedPort == 20:
        print(f"FTP {FailedPort} is closed")
    if FailedPort == 21:
        print(f"FTP {FailedPort} is closed")
    if FailedPort == 22:
        print(f"SSH {FailedPort} is closed")
    if FailedPort == 23:
        print(f"Telnet {FailedPort} is closed")
    if FailedPort == 25:
        print(f"SMTP {FailedPort} is closed")
    if FailedPort == 53:
        print(f"DNS {FailedPort} is closed")
    if FailedPort == 80:
        print(f"HTTP {FailedPort} is closed")
    if FailedPort == 110:
        print(f"POP3 {FailedPort} is closed")
    if FailedPort == 143:
        print(f"IMAP {FailedPort} is closed")
    if FailedPort == 443:
        print(f"HTTPS {FailedPort} is closed")
