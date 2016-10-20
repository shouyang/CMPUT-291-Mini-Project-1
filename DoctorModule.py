# Author : Daniel Zhou
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime

def DOC_A(conn,StaffID,StaffName):
	print("Function A has been called.")
	return 0
def DOC_B(conn,StaffID,StaffName):
	print("Function B has been called.")
	return 0
def DOC_C(conn,StaffID,StaffName):
	print("Function C has been called.")
	return 0
def DOC_D(conn,StaffID,StaffName):
	print("Function D has been called.")
	return 0
def DOC_E(conn,StaffID,StaffName):
	print("Logging Off")
	conn.Close()
	return 0

def DOC_Text(StaffID,StaffName):
	print ("\n")
	print ("Doctor Module")
	print ( str(StaffID) + " | " + str(StaffName) + " | " + str(datetime.datetime.now() ) )
	print ("====")
	print ("A - View Charts By Patient")
	print ("B - Open Chart & Add Symptom")
	print ("C - Open Chart & Add Diagnosis")
	print ("D - Open Chart & Add Medication")
	print ("E - Logout and Exit")
	print ("====")

def DOC(conn = sqlite3.connect("hospital.db"), StaffID = "111", StaffName = "John Doe"):
	# <TODO> Consider conn the sql database connection
	while True:
		DOC_Text(StaffID,StaffName)
		USR_Selection = str(raw_input("OPTION> "))
		# Functional Choices
		if USR_Selection.upper() == "A":
			DOC_A(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "B":
			DOC_B(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "C":
			DOC_C(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "D":
			DOC_D(conn,StaffID,StaffName)
		elif USR_Selection.upper() == "E":
			DOC_E(conn,StaffID,StaffName)
			break
		# Other Unrecognized input
		else:
			print ("Input Not valid, Retry")	
			continue
if __name__ == "__main__":
    DOC()


