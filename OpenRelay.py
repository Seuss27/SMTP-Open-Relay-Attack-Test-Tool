import socket
import smtplib

IP = input("Enter IP address: ")
Port = input("Enter Port Number: ")

X = input("From: ")
Y = input("TO: ")

s = socket.socket()
s.connect((IP, int(Port)))
socket.setdefaulttimeout(3)

ans = s.recv(1024)


if '220' in str(ans):
    print("\n[+]Port {} open on the target system\n".format(Port))
    smtpserver = smtplib.SMTP(IP, int(Port))
    r = smtpserver.docmd("Mail From:", X)
    a = str(r)
    if "250" in a:
        r = smtpserver.docmd("RCPT TO:", Y)
        a = str(r)
        if "250" in a:
            
            print("[+]The target system seems vulenarble to Open relay attack")

        else:
            print("[-]The target system is not vulnerable to Open relay attack")
        
    
else:
    print("[-]Port is closed/Filtered")
