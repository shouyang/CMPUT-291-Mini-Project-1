# Author : Chris Saunders
# Function : Module to handle tasks related to Admin.

import sqlite3
import datetime

def Start_Date(): #Asks for the Year/Month/Day and creates a date object
	print("Please enter the year of the start date (YYYY)")
	try:
		start_date_year = int(raw_input("Starting Year> "))
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		return 0

	print("Please enter the month of the start date (MM)")
	try:
		start_date_month = int(raw_input("Starting Month> "))
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		return 0

	print("Please enter the day of the start date (DD)")
	try:
		start_date_day = int(raw_input("Starting Day> "))
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		return 0
	

	try: #After getting the dates it creates the object
		start_date = datetime.date(start_date_year,start_date_month,start_date_day)
		return start_date
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		print e
		return 0

def End_Date(): #Asks for the Year/Month/Day and creates a date object same as above
	print("Please enter the year of the end date (YYYY)")
	try:
		end_date_year = int(raw_input("End Year> "))
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		return 0
	
	print("Please enter the month of the end date (MM)")
	try:
		end_date_month = int(raw_input("End Month> "))
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		return 0
	
	print("Please enter the day of the End date (DD)")
	try:
		end_date_day = int(raw_input("End Day> "))
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		return 0
	
	try:
		end_date = datetime.date(end_date_year,end_date_month,end_date_day)
		return end_date
	except Exception as e:
		print('\n')
		print("Date Entry Error, Returning To Main Menu")
		print e
		return 0

def Date_Check(start_date,end_date,target_date): #Checks if target_date is within the two other dates
	if start_date < target_date and target_date < end_date:
		return True
	else:
		return False

def ADM_A(conn,StaffID,StaffName):
	print("Function A has been called.")
	start_date = Start_Date()
	if start_date == 0: #If the start date fails
		return 0
	end_date = End_Date()
	if end_date == 0: #If the end date fails
		return 0

	if start_date > end_date: #If start date comes after end date chronologically
		print("Error: Start date must precede end date")
		return 0


	query = "SELECT staff_id, mdate, SUM(amount), drug_name"\
	" FROM medications"\
	" GROUP BY staff_id, drug_name, mdate"\
	" ORDER BY staff_id, drug_name" #Query for the DB
	cursor = conn.cursor()
	cursor.execute(query)
	oldID = None #For counting all the drugs under each doctor
	oldDrug = None #for summing all the drugs under each doctor
	drugTotal = 0 #Count for a given drug under a given doctor
	for row in cursor:
		newID = row[0]
		newDrug = row[3]
		temp = row[1] #Just holds the mdate for the next line
		current_date = datetime.date(int(temp[0:4]), int(temp[5:7]), int(temp[8:10])) #Makes a date object
		if Date_Check(start_date, end_date, current_date): #Checks mdate is within the period
			if str(newDrug) != str(oldDrug) and oldDrug != None: #Prints out a total of the drug
				print('Prescribed ' + str(drugTotal) + ' units of ' + str(oldDrug))
				drugTotal = 0

			if newID != oldID or oldID == None: #Prints the ID of the doctor
				print('==============')
				print("Doctor ID: " + str(row[0]))
			
			oldID = newID
			oldDrug = newDrug
			drugTotal += row[2]
	if str(newDrug) == str(oldDrug) and drugTotal != 0: #Special check in case the last row doesnt print
		print('Prescribed ' + str(drugTotal) + ' units of ' + str(oldDrug))
		drugTotal = 0
	return 0

def TEST_B(cursor, cat): #Actually handles printing some lines, not just a test anymore
	for x in cursor:
		if x[0] == cat:
			print(str(x[3]) + ' units of the drug ' + str(x[1]) + ' have been prescribed in the period')

def ADM_B(conn,StaffID,StaffName):
	print("Function B has been called.")
	start_date = Start_Date()
	if start_date == 0: #If the start date fails
		return 0
	end_date = End_Date()
	if end_date == 0: #If the end date fails
		return 0

	if start_date > end_date: #If start date comes after end date chronologically
		print("Error: Start date must precede end date")
		return 0
	query1 = 'SELECT Category, m.drug_name, m.amount, SUM(m.amount) '\
	'FROM medications m, drugs d '\
	'WHERE m.drug_name = d.drug_name AND CAST(m.mdate AS DATE) > CAST(%s AS DATE) AND CAST(m.mdate AS DATE) < CAST(%s AS DATE) '\
	'GROUP BY d.category, d.drug_name' %(start_date.__str__(),end_date.__str__())
	
	query2 = 'SELECT Category, SUM(m.amount) '\
	'FROM medications m, drugs d '\
	'WHERE m.drug_name = d.drug_name AND CAST(m.mdate AS DATE) > CAST(%s AS DATE) AND CAST(m.mdate AS DATE) < CAST(%s AS DATE) '\
	'GROUP BY Category'  %(start_date.__str__(),end_date.__str__())
	cursor1 = conn.cursor()
	cursor1.execute(query1)
	cursor2 = conn.cursor()
	cursor2.execute(query2)

	print('\n')
	for row in cursor2:
		print('Drug Category Name: ' + str(row[0]))
		cursor1.execute(query1)
		TEST_B(cursor1, str(row[0]))
		print('Totalling ' + str(row[1]) + ' units')
		print('==============')
		
	# for x in cursor1:
	# 	print(str(x[3]) + ' units of the drug ' + str(x[1]) + ' have been prescribed in the period')
	# for row in cursor2:
	# 	print('Overall ' + str(row[1]) + ' units of the category ' + str(row[0]) + ' have been prescribed in the period')


	return 0



def ADM_C(conn,StaffID,StaffName):
	print("Function C has been called.")
	print("Please enter the diagnosis")
	diagnosis = str(raw_input())
	chart = []
	query1 = "Select chart_id, ddate FROM diagnoses WHERE diagnosis Like '%s' COLLATE NOCASE" %(diagnosis)
	cursor1 = conn.cursor()
	cursor1.execute(query1)
	for row in cursor1:
		chart.append((str(row[0]), str(row[1]))) #Gets a list of all charts/dates that had a diagnoses given

	print("Medications given to patients after they have been diagnosed with %s in decending order: " %(diagnosis))
	i = 0
	drugDict = {}
	for i in range(len(chart)):
		temp = chart[i][1]
		ddate = datetime.date(int(temp[0:4]), int(temp[5:7]), int(temp[8:10])) #Diagnosis date
		query2 = 'SELECT drug_name, mdate'\
		' FROM medications'\
		' WHERE %s = chart_id' %(str(chart[i][0]))
		cursor2 = conn.cursor()
		cursor2.execute(query2) #Gets the drugs and the date they were administered to a chart that has the diagnosis
		for row in cursor2:
			temp = row[1]
			mdate = datetime.date(int(temp[0:4]), int(temp[5:7]), int(temp[8:10])) #Medication date
			if mdate > ddate: #If medication came after diagnosis
				drugDict[str(row[0])] = drugDict.get(row[0], 0) + 1
		i +=1
	temp = sorted(drugDict, key=drugDict.__getitem__, reverse =True) #Sorted by how much medication was given
	for item in temp:
		print(item)

	return 0




def ADM_D(conn,StaffID,StaffName): 
	print("Function D has been called.")
	print("Please enter a drug name: ")
	drug = str(raw_input()) #Drug of interest
	chart =[] #a list of tuples containing the chart id and date the drug was administered
	query1 = "Select  m.chart_id, m.mdate FROM medications m Where m.drug_name LIKE '%s'" %(drug)
	cursor1 = conn.cursor()
	cursor1.execute(query1)
	for row in cursor1:
		chart.append((str(row[0]), str(row[1]))) #Makes the list of tuples
	print("Diagnoses that have been made prior to prescribing the drug: %s" %(drug))
	i = 0
	diagDict = {} #key = diagnosis value = tuple containing (total,number of times prescribed)
	for i in range(len(chart)):
		temp = chart[i][1] #Date of medication
		mdate = datetime.date(int(temp[0:4]), int(temp[5:7]), int(temp[8:10])) #Date of medication as a date object
		query2 = "SELECT d.diagnosis, d.ddate, m.amount FROM diagnoses d, medications m"\
		" WHERE %s = d.chart_id AND drug_name LIKE '%s' COLLATE NOCASE" %(str(chart[i][0]), drug)
		cursor2 = conn.cursor()
		cursor2.execute(query2)#Gets the diagnosis a drug was administered for on a ddate in an amount
		for row in cursor2:
			temp = row[1]
			ddate = datetime.date(int(temp[0:4]), int(temp[5:7]), int(temp[8:10]))
			if mdate > ddate: #If the diagnosis came before the drug was given
				amount = row[2] #Amount of drug prescribed
				if str(row[0]) in diagDict: #stores data for each diagnosis, how much a drug was given how many times
					diagDict[str(row[0])][0] += amount
					diagDict[str(row[0])][1] +=1
				else:
					diagDict[str(row[0])] = []
					diagDict[str(row[0])].append(amount)
					diagDict[str(row[0])].append(1)
		i += 1
	avgDict = {} #Computes the average amount of drug prescribed for each diagnoses
	for key in diagDict:
		avgDict[key] = int(diagDict[key][0]) / int(diagDict[key][1])
	temp = sorted(avgDict, key=avgDict.__getitem__, reverse =True) #Sorted by average
	for item in temp:
		print(item) #Success?



	return 0





def ADM_E(conn,StaffID,StaffName):
	print("Logging Off")
	conn.Close()
	return 0

def ADM_Text(StaffID,StaffName):
	print ("\n")
	print ("Admin Module")
	print ( str(StaffID) + " | " + str(StaffName) + " | " + str(datetime.datetime.now() ) )
	print ("====")
	print ("A - View Drugs Prescribed By Each Doctor For A Specific Period")
	print ("B - View Drugs By Category That Were Prescribed in a Specific Period")
	print ("C - View All Drugs Presribed After A Specific Diagnosis")
	print ("D - View All Diagnoses That Preceded a Specific Drug")
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


