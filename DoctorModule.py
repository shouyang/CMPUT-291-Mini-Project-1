# Author : Daniel Zhou, Jordan Vogel
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime
from operator import itemgetter

def DOC_A(conn,StaffID,StaffName):
	cursor = conn.cursor()
	cursor.execute("SELECT p.hcno FROM patients p")
	hcno_list = cursor.fetchall()
	hcnoList = []
	for i in hcno_list:
		hcnoList.append(i[0])
	while True:
		patient_name = raw_input ("Enter patient hcno: ")
		if patient_name not in hcnoList:
			print("Invalid patient HCNO, please try again.")
		else:
			break
		
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
		cursor.execute("SELECT s.symptom, s.obs_date FROM charts c, symptoms s WHERE s.chart_id = c.chart_id AND c.chart_id = '%d' " %select_chart)
		print ("Chart number: "+str(select_chart))
		sym_list = cursor.fetchall()
		print(sym_list)
		cursor.execute("SELECT d.diagnosis, d.ddate FROM charts c, diagnoses d WHERE d.chart_id = c.chart_id AND c.chart_id = '%d' " %select_chart)
		diag_list = cursor.fetchall()
		print(diag_list)
		cursor.execute("SELECT m.drug_name, m.mdate, m.start_med, m.end_med, m.amount FROM charts c, medications m WHERE m.chart_id = c.chart_id AND c.chart_id = '%d' " %select_chart)
		med_list = cursor.fetchall()
		print(med_list)
		

	return 0

def DOC_B(conn,StaffID,StaffName):
	
	cursor = conn.cursor()
	cursor.execute("SELECT p.hcno FROM patients p")
	hcno_list = cursor.fetchall()
	hcnoList = []
	for i in hcno_list:
		hcnoList.append(i[0])
	while True:
		patient_name = raw_input ("Enter patient hcno: ")
		if patient_name not in hcnoList:
			print("Invalid patient HCNO, please try again.")
		else:
			break
		
			
	print ("Open charts for patient number " + patient_name + ":")
	chart_number_list = []
	
	if patient_name.isdigit():
		patient_name = int(patient_name)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_name)
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list:
			chart_number_list.append(int(i[0]))
			if i[3] == None:
				#print ("Open charts for patient: "+str(patient_name))
				print("Chart "  + i[0])
				
		print ("====")
		select_chart = int(raw_input ("Enter open chart number: "))
		if select_chart not in chart_number_list:
			print("Invalid chart ID")
		else:
			symptom_text = raw_input("Enter symptom: ")
			cursor.execute( "INSERT INTO symptoms VALUES (?,?,?,?,?)", (int(patient_name), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(symptom_text) ))
			conn.commit()	
					
				
	return 0

def DOC_C(conn,StaffID,StaffName):
	
	cursor = conn.cursor()
	cursor.execute("SELECT p.hcno FROM patients p")
	hcno_list = cursor.fetchall()
	hcnoList = []
	for i in hcno_list:
		hcnoList.append(i[0])	
	while True:
		patient_name = raw_input ("Enter patient hcno: ")
		if patient_name not in hcnoList:
			print("Invalid patient HCNO, please try again.")
		else:
			break
	print ("Open charts for patient number " + patient_name + ":")
	chart_number_list = []
	
	if patient_name.isdigit():
		patient_name = int(patient_name)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_name)
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list:
			chart_number_list.append(int(i[0]))
			if i[3] == None:
				#print ("Open charts for patient: "+str(patient_name))
				print("Chart "  + i[0])
				
		print ("====")	
		select_chart = int(raw_input ("Enter open chart number: "))
		if select_chart not in chart_number_list:
			print("Invalid chart ID")
		else:
			diagnoses_text = raw_input("Enter diagnoses: ")
			cursor.execute( "INSERT INTO diagnoses VALUES (?,?,?,?,?)", (int(patient_name), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(diagnoses_text) ))
			conn.commit()
			
			
	return 0

def DOC_D(conn,StaffID,StaffName):
	cursor = conn.cursor()
	cursor.execute("SELECT p.hcno FROM patients p")
	hcno_list = cursor.fetchall()
	hcnoList = []
	for i in hcno_list:
		hcnoList.append(i[0])
	while True:
		patient_name = raw_input ("Enter patient hcno: ")
		if patient_name not in hcnoList:
			print("Invalid patient HCNO, please try again.")
		else:
			break
		
	print ("Open charts for patient number " + patient_name + ":")
	chart_number_list = []
		
	if patient_name.isdigit():
		patient_name = int(patient_name)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_name)
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list:
			chart_number_list.append(int(i[0]))
			if i[3] == None:
				#print ("Open charts for patient: "+str(patient_name))
				print("Chart "  + i[0])
				
		print ("====")	
		select_chart = int(raw_input ("Enter open chart number: "))
		if select_chart not in chart_number_list:
			print("Invalid chart ID")
		else:
			medication_name = raw_input("Enter drug name: ")
			start_med = raw_input("Enter start date in YYYY-MM-DD format: ")
			end_med = raw_input("Enter ending date in YYYY-MM-DD format: ")
			amount = raw_input("Enter drug amount: ")
			
			
			cursor.execute("INSERT INTO medications VALUES (?,?,?,?,?,?,?,?)", (int(patient_name), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(start_med), str(end_med), str(amount), str(medication_name)))
			conn.commit()
	
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


