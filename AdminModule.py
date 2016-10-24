# Author : Chris Saunders
# Function : Module to handle tasks related to Admin.

import sqlite3
import datetime
class doctor: #Doctor object to store drugs perscribed for ADM_A
	drugs = dict()
	id = ''

	def __init__(self, id):
		self.id = id

def Start_Date(): #Asks for the Year/Month/Day and creates a date object
	print("Please enter the year of the start date (YYYY)")
	start_date_year = int(raw_input("Starting Year> "))
	
	print("Please enter the month of the start date (MM)")
	start_date_month = int(raw_input("Starting Month> "))

	print("Please enter the day of the start date (DD)")
	start_date_day = int(raw_input("Starting Day> "))

	try: #After getting the dates it creates the object
		start_date = datetime.date(start_date_year,start_date_month,start_date_day)
		return start_date
	except Exception as e:
		print('\n')
		print("Date Entry Error")
		print e
		return 0

def End_Date(): #Asks for the Year/Month/Day and creates a date object same as above
	print("Please enter the year of the end date (YYYY)")
	end_date_year = int(raw_input("End Year> "))
	print("Please enter the month of the end date (MM)")
	end_date_month = int(raw_input("End Month> "))
	print("Please enter the day of the End date (DD)")
	end_date_day = int(raw_input("End Day> "))
	try:
		end_date = datetime.date(end_date_year,end_date_month,end_date_day)
		return end_date
	except Exception as e:
		print('\n')
		print("Date Entry Error")
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


	query = "SELECT staff_id, mdate, amount, drug_name FROM medications"
	cursor = conn.cursor()
	cursor.execute(query)
	doctorDict = dict()
	i = 0
	for row in cursor:
		temp = row[1] #Just holds the mdate for the next line
		current_date = datetime.date(int(temp[0:4]), int(temp[5:7]), int(temp[8:10]))
		if Date_Check(start_date, end_date, current_date): #Checks mdate is within the period
			if row[0] in doctorDict: #If the doctors id is in the dictionary
				if row[3] in doctorDict[row[0]].drugs: #If the drug has been prescribed before by the doctor
					doctorDict[row[0]].drugs[row[3]] += row[2]
				else: #Doctor exists but its a new medication
					doctorDict[row[0]].drugs[row[3]] = row[2] #Creates a Dictionary entry for the doctor object
			else:# If the id is not in the dictionary
				doctorDict[row[0]] = doctor(row[0])  #Creates a dicitonary entry with the id as a key and a doctor object as a value
				doctorDict[row[0]].drugs[row[3]] = row[2] #Creates a Dictionary entry for the doctor object
				#The key is the drug name the value is the amount
	for x in doctorDict: #Print out
		print("Doctor ID: " + x)
		for y in doctorDict[x].drugs:	
			print("Prescribed "+ str(doctorDict[x].drugs[y]) +" units of " + str(y))
		
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
	print ("Admin Module")
	print ( str(StaffID) + " | " + str(StaffName) + " | " + str(datetime.datetime.now() ) )
	print ("====")
	print ("A - View Drugs Prescribed By Each Doctor For A Specific Period")
	print ("B - View Drugs Prescribed By Category For a Specific Period")
	print ("C - View All Drugs Presribed For A Specific Diagnosis")
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


