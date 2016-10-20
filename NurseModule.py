# Author : Daniel Zhou
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime
# Generic Functions
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
# Task Handler Dependents
def NUR_A_MainText():
	print("\n" * 2)
	print("====")
	print("Function A - Create New Chart For Patient")
	print("OPTION 1 REQUIRES: PATIENT ID")
	print("OPTION 2 REQUIRES: PATIENT INFORMATION")
	print("A new chart will be created, admission will be the current time.")
	print("====")
	return 0
# Task Handler Functions
def NUR_A(conn,StaffID,StaffName):
	NUR_A_MainText()
	while True:
		patient_id = raw_input("PATIENT ID (ENTER OR LEAVE BLANK)> ")
		if patient_id == "":
			print("No ID provided, creating new patient record.")
			# Get an unused ID
			query = "SELECT MAX(hcno) FROM patients"
			cursor = conn.cursor()
			cursor.execute(query)
			try:
				auto_id = (int(cursor.fetchone()[0]) + 1) 
			except:
				auto_id = 1
			# Get information from user.
			while True:
				i_hcno = raw_input("HCNO (Leave Blank For Autogeneration)> ")
				if RepresentsInt(i_hcno):
					break
				elif  i_hcno == "":
					i_hcno = str(auto_id)
					break
				else:
					print ("HCNO must be an integer")
					continue
			i_name = raw_input("NAME> ")
			i_age_group = raw_input("AGE GROUP> ")
			i_address = raw_input("ADDRESS> ")
			i_phone = raw_input("PHONE> ")
			i_emg_phone = raw_input("EMG PHONE> ")
			# Print the information for the user to confirm. 
			print("==")
			print("HCNO: " + i_hcno)
			print("NAME: " + i_name)
			print("AGE GROUP: " + i_age_group)
			print("ADDRESS: " + i_address)
			print("PHONE: " + i_phone)
			print("EMG PHONE: " + i_emg_phone)
			
			usr_confirm = raw_input("CONFIRM? (Y/N/Q)> ").upper()
			if usr_confirm == "Y":	
				query = "INSERT INTO patients VALUES (?,?,?,?,?,?);"
				try:
					cursor.execute(query,(i_hcno,i_name,i_age_group,i_address,i_phone,i_emg_phone))
					conn.commit()
					print ("Patient Creation Sucessful.")
					break
				except Exception, e:
					print ("Database rejected entry")
					print (e)
					print ("==")
					print ("Retry Entry")
					print ("\n" * 3)
					continue
			elif usr_confirm == "Q":
				print ("Quit Selected")
				break
			else:
				print("No confirmation selected")
				print("Restarting Entry")
				print ("\n" * 3)
				continue
		elif RepresentsInt(patient_id): # Enters a valid integer
			if True: # Valid HCNO
				pass 
			else:	 # Unknown HCNO
				pass

		else:
			pass
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
	print("Logging Off")
	conn.Close()
	return 0

def NUR_Text(StaffID,StaffName):
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

def NUR(conn = sqlite3.connect("hospital.db"), StaffID = "111", StaffName = "John Doe"):
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


