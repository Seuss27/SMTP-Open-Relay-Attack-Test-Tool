import socket
import smtplib
import configparser

config = configparser.ConfigParser()
config.read('OpenRelay.ini')

IP = input("Enter IP address: ")
Port = input("Enter Port Number: ")

to_address = config['DEFAULT']['ToAddress']
from_address = config['DEFAULT']['FromAddress']


def smtp_connect(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    socket.setdefaulttimeout(3)

    return s.recv(1024)


def is_open(answer):
    if '220' in str(answer):
        return True


def check_success(answer):
    if '250' in str(answer):
        return True
    else:
        return False


def test_relay(ip, port):
    smtpserver = smtplib.SMTP(ip, int(port))
    r = smtpserver.docmd("Mail From:", from_address)
    #  Check for the 250 return value from the server from
    if check_success(r):
        r = smtpserver.docmd("RCPT TO:", to_address)
        #  return the response check from the to
        return check_success(r)
    else:
        # If it gives another value it is not vulnerable
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