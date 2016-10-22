# Author : Daniel Zhou
# Function : Program's central function

import sqlite3
import datetime
import base64
import getpass # Used to hide passwords on input prompts
import hashlib
from DoctorModule import * 
from NurseModule import * 
from AdminModule import * 

# Login Text
def login_menu():
    print ("\n")
    print("CMPUT 291 - Mini Project 1")
    print("Hospital Database System")
    print("====")
    print("A - Login as Existing User")
    print("B - Create New User")
    print("C - Exit")
    print("====")
    print("Choose an option by typing in the corresponding letter.")
    # Handles user menu choice
    while True:
        usr_input = raw_input("OPTION> ")
        if usr_input.upper() in ('A','B', 'C'):
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
            print (identifier)
            dblink = input("Please input the path to the SQLite 3 DB: ")
# Login Functions
def login_main(conn):
    while True:  
        # Get user input
        print("Please provide a username and password.")
        username = raw_input("Username: ")
        password = str(getpass.getpass("Password (Input Hidden): "))

        # Encrypt the password, such that we can compare against the encrypted password.capitalize
        password = hashlib.sha224(password).hexdigest()

        # Query database for matching profiles.
        cursor = conn.cursor()
        cursor.execute("SELECT staff_id, name, role, login FROM staff WHERE login = ? AND password = ?", (username,password))
        # Allow user to select the login they require.
        for row in cursor:      
                print ("Staff_id: " + str(row[0]) )
                print ("Name: " + str(row[1]) )
                print ("Role: "  + str(row[2]) )
                print ("Login: "  + str(row[3]) )
                while  True:
                    print ("Use this account?")
                    user_sel = raw_input("OPTION (Y/N)>").upper()
                    if user_sel == "Y":
                        return [str(row[0]), str(row[1]), str(row[2]), str(row[3])]
                    elif user_sel == "N":
                        break
                    else:
                        print ("Input Unrecognized.")
        # Should only run if login is unrecognized.
        print ("Login Unknown / Invalid or reached end of accounts found.")
        print ("Please retry.")
        continue
    return 0
def login_create(conn):
    # Disalllows access to most people.
    if  "DEMO123" != str(getpass.getpass("Provide Key Phrase: ")):
        return 0

    print("Please provide a username and password to create a new account.")
    # Basic Identification Information
    username = raw_input("Username: ")
    name     = raw_input("Name: ")
    # Role Selection
    while True:
        role = raw_input("Role (D/N/A): ")
        if role.upper() in ('D','N','A'):
            role = str(role.upper())
            break
        else:
            print("Please select fron the valid roles of (D/N/A)")
            continue
    # Password Selection with Confirmation
    while True:
        password = str(getpass.getpass("Password: "))
        print ("Please confirm your password (Input Hidden):")
        password_confirmation = str(getpass.getpass("Password: "))

        if password == password_confirmation:
            # Encryption
            password = hashlib.sha224(password).hexdigest()
            # Find a suitable ID for this entry
            query = "SELECT MAX(staff_id) FROM staff"
            cursor = conn.cursor()
            cursor.execute(query)
            ID = int(cursor.fetchone()[0]) + 1
            # Execute the query to create new account
            Values = (str(ID),str(role),str(name),str(username),str(password))
            cursor.execute("INSERT INTO staff values (?,?,?,?,?)",Values)
            conn.commit()

            print ("Account Creation Sucessful")
            break
        else:
            print ("Password and Password Confirmation were not the same.")
            print ("Please retry the Password and Password Confirmation prompt.")
            continue
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
    while  True:
        usr_input = login_menu()
        if usr_input == 'A':
            staff_id,name,role,username = login_main(conn)
            if role == "D":
                DOC(conn,staff_id,name)
            elif role == "N":
                NUR(conn,staff_id,name)
            elif role == "A":
                ADM(conn,staff_id,name)
            else:
                print ("Role not recognized")
        elif usr_input == 'B':
            login_create(conn)
        elif usr_input == 'C':
            break
        # Get associated information, connect to module.
    
    
if __name__ == "__main__":
    main()
