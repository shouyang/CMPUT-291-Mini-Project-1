# Author : Daniel Zhou
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime

def ADM_A(conn,StaffID,StaffName):
	print("Function A has been called.")
	return 0
def ADM_B(conn,StaffID,StaffName):
	print("Function B has been called.")
	return 0
def ADM_C(conn,StaffID,StaffName):
	print("Function C has been called.")
	return 0
def ADM_D(conn,StaffID,StaffName):
	print("Function D has been called.")
	return 0
def ADM_E(conn,StaffID,StaffName):
	print("Logging Off")
	conn.Close()
	return 0

def ADM_Text(StaffID,StaffName):
	print ("\n")
	print ("Nurse Module")
	print ( str(StaffID) + " | " + str(StaffName) + " | " + str(datetime.datetime.now() ) )
	print ("====")
	print ("A - Create New Chart For Patient")
	print ("B - Close Chart For Patient")
	print ("C - View Charts By Patient")
	print ("D - Open Chart & Add Symptom")
	print ("E - Logout and Exit")
	print ("====")

def ADM(conn = sqlite3.connect("hospital.db"), StaffID = "111", StaffName = "John Doe"):
	# <TODO> Consider conn the sql database connection
	while True:
		ADM_Text(StaffID,StaffName)
		USR_Selection = str(raw_input("OPTION> "))
		# Functional Choices
		if USR_Selection.upper() == "A":
			ADM_A(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "B":
			ADM_B(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "C":
			ADM_C(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "D":
			ADM_D(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "E":
			ADM_E(conn,StaffID,StaffName)
			break
		# Other Unrecognized input
		else:
			print ("Input Not valid, Retry")	
			continue
if __name__ == "__main__":
    ADM()


