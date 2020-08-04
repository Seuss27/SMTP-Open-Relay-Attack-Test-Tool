import socket
import smtplib

IP = input("Enter IP address: ")
Port = input("Enter Port Number: ")

X = input("From: ")
Y = input("TO: ")


def smtp_connect(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    socket.setdefaulttimeout(3)

    return s.recv(1024)


def is_open(answer):
    if '220' in str(answer):
        return True


def test_relay(ip, port):
    smtpserver = smtplib.SMTP(IP, int(Port))
    r = smtpserver.docmd("Mail From:", X)
    a = str(r)
    if "250" in a:
        r = smtpserver.docmd("RCPT TO:", Y)
        a = str(r)
        if "250" in a:
            return True
        else:
            return False


ans = smtp_connect(IP, Port)

if is_open(ans):
    print("\n[+]Port {} open on the target system\n".format(Port))
    if test_relay(IP, Port):
        print("[+]The target system seems vulenarble to Open relay attack")
    else:
        print("[-]The target system is not vulnerable to Open relay attack")
else:
    print("[-]Port is closed/Filtered")