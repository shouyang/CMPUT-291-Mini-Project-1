# Author : Daniel Zhou, Jordan Vogel
# Function : Module to handle tasks related to doctors.

import sqlite3
import datetime
from operator import itemgetter

def DOC_A(conn,StaffID,StaffName):
	cursor = conn.cursor() #initialize the cursor to the connection
	cursor.execute("SELECT p.hcno FROM patients p") #get all the patient numbers
	hcno_list = cursor.fetchall()
	hcnoList = [] #add them all to a list 
	for i in hcno_list:
		hcnoList.append(i[0])
	while True: #loop to check if the pateint name is in the list of registered patients
		try:
			patient_num = raw_input ("Enter patient hcno: ")
			if patient_num not in hcnoList:
				print("Invalid patient HCNO, please try again.")
			else:
				break
		except ValueError:
			print("Must enter a valid number. Please try again.")
		
	print ("Charts for patient number " + patient_num + ":")
	chart_number_list = []
	
	if patient_num.isdigit(): #checks to see if the patient name is infact a number
		patient_num = int(patient_num)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_num) #query to to get all charts matching the patient number
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list: #this loop checks to see if the charts are open or closed and returns them as such
			chart_number_list.append(int(i[0]))
			
			if i[3] == None:				
				print("Chart " + i[0] + " is open")
			else:
				print("Chart " + i[0] + " is closed")
		
	print("====")
	select_chart = int(raw_input ("Enter desired chart number: "))#gets input for selected chart
	
	if select_chart not in chart_number_list: #checks if the chart number is valid
		print ("Invalid chart number entry")
	else: # if the chart numnber is valid continue operation
		cursor.execute("SELECT s.symptom, s.obs_date FROM charts c, symptoms s WHERE s.chart_id = c.chart_id AND c.chart_id = '%d' " %select_chart)
		print ("Chart number: "+str(select_chart))
		sym_list = cursor.fetchall()

		cursor.execute("SELECT d.diagnosis, d.ddate FROM charts c, diagnoses d WHERE d.chart_id = c.chart_id AND c.chart_id = '%d' " %select_chart)
		diag_list = cursor.fetchall()

		cursor.execute("SELECT m.drug_name, m.mdate, m.start_med, m.end_med, m.amount FROM charts c, medications m WHERE m.chart_id = c.chart_id AND c.chart_id = '%d' " %select_chart)
		med_list = cursor.fetchall()

		total_list = diag_list + med_list + sym_list
		total_list.sort(key = lambda x: x[1]) #little hack to arrange the sum of 3 lists by a single index in each list
		print("Symptoms, Diagnoses and Medications for patient number: "+ str(patient_num) + "\n" + "====")
		for item in total_list:
			if len(item) > 2:#prints the medications items which are a tuple longer than 2 items
				for j in item:
					print j, 
			else:
				print(item[0]+" "+item[1]) # prints the two item tuples from diagnoses and symptoms
		

	return 0

def DOC_B(conn,StaffID,StaffName):
	cursor = conn.cursor() #initialize the cursor to the connection
	cursor.execute("SELECT p.hcno FROM patients p") #get all the patient numbers
	hcno_list = cursor.fetchall()
	hcnoList = [] #add them all to a list 
	for i in hcno_list:
		hcnoList.append(i[0])
	while True: #loop to check if the pateint name is in the list of registered patients
		try:
			patient_num = raw_input ("Enter patient hcno: ")
			if patient_num not in hcnoList:
				print("Invalid patient HCNO, please try again.")
			else:
				break
		except ValueError:
			print("Must enter a valid number. Please try again.")
		
	print ("Open charts for patient number " + patient_num + ":")
	chart_number_list = []
	
	if patient_num.isdigit(): #checks to see if the patient name is infact a number
		patient_num = int(patient_num)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_num) #query to to get all charts matching the patient number
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list: #this loop checks to see if the charts are open or closed and returns them as such
			chart_number_list.append(int(i[0]))
			if i[3] == None:
				#print ("Open charts for patient: "+str(patient_num))
				print("Chart "  + i[0])
				
		print ("====")
		select_chart = int(raw_input ("Enter open chart number: ")) #opens selected chart
		if select_chart not in chart_number_list:
			print("Invalid chart ID")
		else:
			symptom_text = raw_input("Enter symptom: ") #gathers symptom data from user
			cursor.execute( "INSERT INTO symptoms VALUES (?,?,?,?,?)", (int(patient_num), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(symptom_text) ))
			#above line inserts the entered data into the symptoms table, with the date set to current
			conn.commit()	
					
				
	return 0

def DOC_C(conn,StaffID,StaffName):
	cursor = conn.cursor() #initialize the cursor to the connection
	cursor.execute("SELECT p.hcno FROM patients p") #get all the patient numbers
	hcno_list = cursor.fetchall()
	hcnoList = [] #add them all to a list 
	for i in hcno_list:
		hcnoList.append(i[0])
	while True: #loop to check if the pateint name is in the list of registered patients
		try:
			patient_num = raw_input ("Enter patient hcno: ")
			if patient_num not in hcnoList:
				print("Invalid patient HCNO, please try again.")
			else:
				break
		except ValueError:
			print("Must enter a valid number. Please try again.")
		
	print ("Open charts for patient number " + patient_num + ":")
	chart_number_list = []
	
	if patient_num.isdigit(): #checks to see if the patient name is infact a number
		patient_num = int(patient_num)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_num) #query to to get all charts matching the patient number
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list: #this loop checks to see if the charts are open or closed and returns them as such
			chart_number_list.append(int(i[0]))
			if i[3] == None:
				#print ("Open charts for patient: "+str(patient_num))
				print("Chart "  + i[0])
				
		print ("====")	
		select_chart = int(raw_input ("Enter open chart number: ")) #select desired chart
		if select_chart not in chart_number_list:
			print("Invalid chart ID")
		else:
			diagnoses_text = raw_input("Enter diagnoses: ") #gathers diagnosis data from user
			cursor.execute( "INSERT INTO diagnoses VALUES (?,?,?,?,?)", (int(patient_num), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(diagnoses_text) ))
			#query to insert the data into the diagnoses table
			conn.commit()
			
			
	return 0

def DOC_D(conn,StaffID,StaffName):
	cursor = conn.cursor() #initialize the cursor to the connection
	cursor.execute("SELECT p.hcno FROM patients p") #get all the patient numbers
	hcno_list = cursor.fetchall()
	hcnoList = [] #add them all to a list 
	for i in hcno_list:
		hcnoList.append(i[0])
	while True: #loop to check if the pateint name is in the list of registered patients
		try:
			patient_num = raw_input ("Enter patient hcno: ")
			if patient_num not in hcnoList:
				print("Invalid patient HCNO, please try again.")
			else:
				break
		except ValueError:
			print("Must enter a valid number. Please try again.")
		
	print ("Open charts for patient number " + patient_num + ":")
	chart_number_list = []
	
	if patient_num.isdigit(): #checks to see if the patient name is infact a number
		patient_num = int(patient_num)
		cursor.execute("SELECT * FROM charts WHERE charts.hcno = '%d'" % patient_num) #query to to get all charts matching the patient number
		chart_list = cursor.fetchall()
		sorted(chart_list, key = itemgetter(2))
		
		for i in chart_list: #this loop checks to see if the charts are open or closed and returns them as such
			chart_number_list.append(int(i[0]))
			if i[3] == None:
				#print ("Open charts for patient: "+str(patient_num))
				print("Chart "  + i[0])
				
		print ("====")	
		select_chart = int(raw_input ("Enter open chart number: ")) #select desired chart
		if select_chart not in chart_number_list:
			print("Invalid chart ID")
		else:
			alg_list = []
			
			medication_name = raw_input("Enter drug name: ")
			start_med = raw_input("Enter start date in YYYY-MM-DD format: ")
			end_med = raw_input("Enter ending date in YYYY-MM-DD format: ")
			amount = int(input("Enter drug amount in milligrams: "))
			
			cursor.execute("SELECT d.sug_amount FROM dosage d WHERE d.drug_name = '%s'" % medication_name)
			tooMuch = cursor.fetchall()
			
			cursor.execute("SELECT DISTINCT d.age_group FROM dosage d, patients p WHERE d.drug_name = '%s' AND p.age_group = d.age_group" % medication_name)
			drug_age_range = cursor.fetchall()
			
			cursor.execute("SELECT p.age_group FROM patients p WHERE p.hcno = '%d'" % patient_num)
			patient_age_range = cursor.fetchall()	
			
			cursor.execute("SELECT r.drug_name FROM reportedallergies r WHERE r.hcno = '%d' AND r.drug_name = '%s'" % (patient_num, medication_name))
			rep_alg = cursor.fetchall()
			

			
			while True:
				if patient_age_range == drug_age_range:
					if amount > tooMuch[0][0]:
						print("WARNING: Dosage is higher than suggested amount!")
						print("Suggested amount for a patient in this age range is "+str(tooMuch[0][0])+"mg.")
						confirmation = raw_input ("Enter 'y' to continue or press 'n' to change amount: ")
						confirmation = confirmation.lower()
						if confirmation == "n":
							amount = int(input("Enter drug amount in milligrams: "))
						else:
								cursor.execute("INSERT INTO medications VALUES (?,?,?,?,?,?,?,?)", (int(patient_num), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(start_med), str(end_med), str(amount), str(medication_name)))
								conn.commit()	
				elif medication_name == rep_alg[0][0]:
					print
					print("WARNING: Patient has a reported allergy to "+medication_name+":")
					confirmation = raw_input ("Enter 'y' to continue or press 'n' cancel: ")
					confirmation = confirmation.lower()
					if confirmation == "n":
						break
					else:
						cursor.execute("INSERT INTO medications VALUES (?,?,?,?,?,?,?,?)", (int(patient_num), int(select_chart), int(StaffID), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(start_med), str(end_med), str(amount), str(medication_name)))
						conn.commit()	
					break
				break
	
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


