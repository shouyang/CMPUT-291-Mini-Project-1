# Author : Daniel Zhou
# Function : Program's central function

import sqlite3
import datetime
import base64

    
# Make database connection
def create_Connection(dblink):
    while True:
        try:
            conn = sqlite3.connect(dblink)
            return conn
        except expression as identifier:
            print ("The following database could not be found locally")
            print (dblink)
            dblink = input("Please input the path to the SQLite 3 DB: ")

# Password Screen
def login_main(conn):
    print("Please provide a username and password")
    username = input("Username: ")
    password = input("Password: ")


# Basic Encryption and Decryption, requires base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#
# Main
#

def main():
    conn = create_Connection("hospital.db")
    role = login_main(conn)
if __name__ == "__main__":
    main():