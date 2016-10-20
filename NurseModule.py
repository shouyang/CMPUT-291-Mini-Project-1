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
def Get_Input_Fixed_Length(prompt, L):
	while True:
		x = raw_input(prompt)
		if len(x) <= L:
			return x
		else:
			print ("Input Length Exceeds Requirement.")
			continue
def Get_AutoID(conn,key,table):
	# Get an unused ID
	query = "SELECT MAX(" +str(key)+") FROM " + str(table)
	cursor = conn.cursor()
	cursor.execute(query)
	try:
		auto_id = (int(cursor.fetchone()[0]) + 1)
		return auto_id
	except:
		auto_id = 1
		return auto_id

# Task Handler Dependents
	# Function A
def NUR_A_MainText():
	print("\n" * 2)
	print("====")
	print("Function A - Create New Chart For Patient")
	print("OPTION 1 REQUIRES: PATIENT ID")
	print("OPTION 2 REQUIRES: PATIENT INFORMATION")
	print("A new chart will be created, admission will be the current time.")
	print("====")
	return 0
def NUR_A_CreatePatient(conn,StaffID,StaffName,patient_id):
	while True:
		print("\n" * 2)
		print("No ID provided, creating new patient record.")

		auto_id = Get_AutoID(conn,"hcno","patients")
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
		i_name = Get_Input_Fixed_Length("NAME> ",  15)
		i_age_group = Get_Input_Fixed_Length("AGE GROUP> ", 5)
		i_address = Get_Input_Fixed_Length("ADDRESS> ", 30)
		i_phone = Get_Input_Fixed_Length("PHONE (ONLY DIGITS)> ", 10)
		i_emg_phone = Get_Input_Fixed_Length("EMG PHONE (ONLY DIGITS)> ", 10)
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
				cursor = conn.cursor()
				cursor.execute(query,(i_hcno,i_name,i_age_group,i_address,i_phone,i_emg_phone))
				conn.commit()
				print ("Patient Creation Sucessful.")
				return i_hcno
			except Exception, e:
				print ("Database rejected entry")
				print (e)
				print ("==")
				print ("Retry Entry")
				print ("\n" * 3)
				continue
		elif usr_confirm == "Q":
			print ("Quit Selected")
			return 0
		else:
			print("No confirmation selected")
			print("Restarting Entry")
			print ("\n" * 3)
			continue
	return 0
def NUR_A_CheckPatientID(conn, patient_HCNO):
	query = "SELECT COUNT(*) FROM patients WHERE hcno = ?"
	cursor = conn.cursor()
	cursor.execute(query,(patient_HCNO,))
	if int(cursor.fetchone()[0])	> 0:
		return True
	else:
		return False
def NUR_A_CheckOpenCharts(conn,patient_HCNO):
	# Tests to see if there are any unclosed cases for the patient.
	query = "SELECT COUNT(*) FROM charts WHERE hcno = ? AND edate IS NULL"
	cursor = conn.cursor()
	cursor.execute(query,(patient_HCNO,))
	if int(cursor.fetchone()[0])	> 0:
		# There are unclosed cases, must prompt before opening another.
		query = "SELECT * FROM charts WHERE hcno = ?"
		cursor = conn.cursor()
		cursor.execute(query,(patient_HCNO,))
		# Print open cases to user.
		print ("The following open charts for patient: " + str(patient_HCNO) + " have been found.")

		for row in cursor:
			print ("Chart ID: " + str(row[0]) + "| Patient HCNO: " + str(row[1]) + "| Addmission Date: " + str(row[2]))

		return True
	else:
		# There are no unclosed cases, go directly to case creation.
		return False
def NUR_A_CreateChart(conn,patient_HCNO):
	try:
		auto_id = Get_AutoID(conn,"chart_id","charts")
		query = "INSERT INTO charts VALUES (?,?,?,NULL)"
		cursor = conn.cursor()
		cursor.execute(query,(str(auto_id), str(patient_HCNO), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ))
		conn.commit()
		print ("Chart Opened Sucessfully")
		return 0
	except Exception, e:
		print ("Database rejected entry")
		print (e)
		print ("==")
		print ("Retry Entry")
		print ("\n" * 3)
		return 0
def NUR_A_CloseChart(conn,chart_id):
	try:
		query = "UPDATE charts SET edate = ? WHERE chart_id = ?"
		cursor = conn.cursor()
		cursor.execute(query,(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), chart_id ))
		conn.commit()
		print ("Chart Closed Sucessfully")
		return 0
	except Exception, e:
		print ("Database rejected entry")
		print (e)
		print ("==")
		print ("Retry Entry")
		print ("\n" * 3)
		return 0
	# Function B
def NUR_B_MainText():
	print("\n" * 2)
	print("====")
	print("Function B - Close Chart For Patient")
	print("Select Patient and Confirm Chart to Close.")
	print("====")
	return 0
def NUR_B_CheckAllOpenCharts(conn):
	query = "SELECT * FROM charts WHERE edate IS NULL"
	cursor = conn.cursor()
	cursor.execute(query)
	# Print open cases to user.
	print ("The following open charts for patients have been found.")

	for row in cursor:
		print ("Chart ID: " + str(row[0]) + "| Patient HCNO: " + str(row[1]) + "| Addmission Date: " + str(row[2]))

	return 0
# Task Handler Functions
def NUR_A(conn,StaffID,StaffName):
	NUR_A_MainText() # Boiler Plate Text
	while True: # Main Loop
		patient_HCNO = raw_input("PATIENT HCNO (ENTER OR LEAVE BLANK)> ")
		# If input is blank, go to create profile.
		if patient_HCNO == "":
			patient_HCNO = NUR_A_CreatePatient(conn,StaffID,StaffName,patient_HCNO)
			NUR_A_CreateChart(conn,patient_HCNO)
			break
		# If input is a integer.
		elif RepresentsInt(patient_HCNO):
			# If input is a valid hcno.
			if NUR_A_CheckPatientID(conn, patient_HCNO):
				# If input is a valid hcno, and there is atleast one open chart
				if (NUR_A_CheckOpenCharts(conn,patient_HCNO)):
					print ("\n")
					print ("====")
					print ("OPTION A: Close All Existing Charts And Create New")
					print ("OPTION B: Quit And Do Not Create Chart")

					# Allow user to decide what to do with open charts.
					while True:
						usr_sel = str(raw_input("OPTION> ")).upper()
						if usr_sel == 'A':
							cursor = conn.cursor()
							query = "SELECT chart_id FROM charts WHERE hcno = ? AND edate IS NULL"
							cursor.execute(query, (patient_HCNO,))

							for row in cursor:
								NUR_A_CloseChart(conn, str(row[0]))

							NUR_A_CreateChart(conn,patient_HCNO)
							return 0
						if usr_sel == 'B':
							return 0
						else:
							print ("Input Not valid, Retry")
							continue

				# If input is a valid hcno, and there is no open chart.
				else:
					NUR_A_CreateChart(conn,patient_HCNO)
					break
			else:	 # Valid Integer, Unknown HCNO
				print ("No HCNO found. Retry.")
				continue
		else: # Else Main Loop
			print("Input was not blank or a valid integer. Retry.")
			continue
	return 0
def NUR_B(conn,StaffID,StaffName):
	NUR_B_MainText()
	NUR_B_CheckAllOpenCharts(conn)
	while True: # Main Loop
		usr_sel = raw_input("CHART ID> ")
		if RepresentsInt(usr_sel):
			cursor = conn.cursor()
			# Build list of valid choices.
			cursor.execute("SELECT DISTINCT(chart_id) FROM charts WHERE edate IS NULL")
			vaild_charts = []
			for row in cursor:
				vaild_charts.append(int(row[0]))
			# Let user select a value.
			if int(usr_sel) in vaild_charts:
				NUR_A_CloseChart(conn,int(usr_sel))
				break
			else:
				print ("Not a valid chart, retry.")
		else:
			print ("Not a valid Integer, retry.")
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
	print ("A - Create New Chart For Patient Or Create Patient and Open Chart")
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


