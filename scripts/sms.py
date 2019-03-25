#!/usr/bin/env python3
import telnetlib
import sqlite3
import sys

imsi = 999999999999999

def check_extension(extension, conn):
    conn.write("show subscriber extension {}\n".format(extension).encode())
    res = conn.read_until(b"OpenBSC> ")

    if b"No subscriber found for extension" in res:
        create_subscriber(extension, conn)

def create_subscriber(extension, conn):
    conn.write("show subscriber imsi {}\n".format(imsi).encode())
    res = conn.read_until(b"OpenBSC> ")

    if b"No subscriber found for imsi" in res:
        conn.write("subscriber create imsi {}\n".format(imsi).encode())
        conn.read_until(b"OpenBSC> ")

    conn.write(b"enable\n")
    conn.read_until(b"OpenBSC# ")
    conn.write("subscriber imsi {} extension {}\n".format(imsi, extension).encode())
    conn.read_until(b"OpenBSC# ")
    conn.write("subscriber imsi {} name SMSbot\n".format(imsi).encode())
    conn.read_until(b"OpenBSC# ")
    conn.write(b"disable\n")
    conn.read_until(b"OpenBSC> ")


def send(ext_from, ext_to, message):
    conn = telnetlib.Telnet("127.0.0.1", 4242)
    conn.read_until(b"OpenBSC> ")
    check_extension(ext_from, conn)

    conn.write("subscriber extension {} sms sender extension {} send {}\n".format(ext_to, ext_from, message).encode())
    res = conn.read_until(b"OpenBSC> ")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: ./sms.py [extention_from] [extention_to] [\"message\"]")
        sys.exit(1)

    ext_from = sys.argv[1]
    ext_to = sys.argv[2]
    message = sys.argv[3]
    send(ext_from, ext_to, message)