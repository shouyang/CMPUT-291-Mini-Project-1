# Author : Daniel Zhou
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime

def NUR_A(conn,StaffID,StaffName):
	print("Function A has been called.")
	return 0
def NUR_B(conn,StaffID,StaffName):
	print("Function B has been called.")
	return 0
def NUR_C(conn,StaffID,StaffName):
	print("Function C has been called.")
	return 0
def NUR_D(conn,StaffID,StaffName):
	print("Function D has been called.")
	return 0
def NUR_E(conn,StaffID,StaffName):
	print("Function E has been called.")
	return 0

def NUR_Text(StaffID,StaffName):
	print ("Nurse Module")
	print ( str(StaffID) + " | " + str(StaffName) + " | " + str(datetime.datetime.now() ) )
	print ("====")
	print ("A - Create New Chart For Patient")
	print ("B - Close Chart For Patient")
	print ("C - View Charts By Patient")
	print ("D - Open Chart & Add Symptom")
	print ("E - Logout and Exit")
	print ("====")

def NUR(conn = "Test - No Connection", StaffID = "111", StaffName = "John Doe"):
	# <TODO> Consider conn the sql database connection
	while True:
		NUR_Text(StaffID,StaffName)
		USR_Selection = str(raw_input("OPTION> "))
		# Functional Choices
		if USR_Selection.upper() == "A":
			NUR_A(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "B":
			NUR_B(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "C":
			NUR_C(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "D":
			NUR_D(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "E":
			NUR_E(conn,StaffID,StaffName)
			break
		# Other Unrecognized input
		else:
			print ("Input Not valid, Retry")	
			continue
if __name__ == "__main__":
    NUR()


