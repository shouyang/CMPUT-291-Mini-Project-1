# Author : Daniel Zhou
# Function : Program's central function

import sqlite3
import datetime
import base64
# Login Text
def login_menu():
    print("CMPUT 291 - Mini Project 1")
    print("Hospital Database System")
    print("====")
    print("A - Login as Existing User")
    print("B - Create New User")
    print("====")
    print("Choose an option by typing in the corresponding letter.")
    while True:
        usr_input = raw_input("OPTION> ")
        if usr_input.upper() in ('A','B'):
            return usr_input.upper()
        else:
            print ("Input value not valid, please retry your option.")
            continue
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
# Login Functions
def login_main(conn):
    print("Please provide a username and password.")
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    return 0

def login_create(conn):
    print("Please provide a username and password to create a new account.")
    username = raw_input("Username: ")
    password = raw_input("Password: ")
    return 0
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
    # Create Inital Database Connection
    conn = create_Connection("hospital.db")
    # Allow the user to select their inital task
    usr_input = login_menu()
    if usr_input == 'A':
        login_main(conn)
    elif usr_input == 'B':
        login_create(conn)
    # Get associated information, connect to module.
    
    
if __name__ == "__main__":
    main()
