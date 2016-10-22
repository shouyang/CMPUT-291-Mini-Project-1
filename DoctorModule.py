# Author : Daniel Zhou, Jordan Vogel
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime
from operator import itemgetter

def DOC_A(conn,StaffID,StaffName):
	cursor = conn.cursor()
	patient_name = raw_input ("Enter patient hcno: ")
	print ("Charts for patient number " + patient_name + ":")
	chart_number_list = []
	
	if patient_name.isdigit():
		patient_name = int(patient_name)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_name)
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list:
			chart_number_list.append(int(i[0]))
			
			if i[3] == None:				
				print("Chart " + i[0] + " is open")
			else:
				print("Chart " + i[0] + " is closed")
		
	else:
		cursor.execute("SELECT * FROM charts, patients WHERE patients.name = '%s' AND charts.hcno = patients.hcno" % patient_name)
		print(cursor.fetchall())
		
	print("====")
	select_chart = int(raw_input ("Enter desired chart number: "))
	
	if select_chart not in chart_number_list:
		print ("Invalid chart number entry")
	else:
		cursor.execute ("SELECT * FROM charts, symptoms, diagnoses, medications WHERE symptoms.chart_id = '%d' AND medications.chart_id = '%d' AND diagnoses.chart_id = '%d'" % select_chart)
		print(cursor.fetchall())

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


