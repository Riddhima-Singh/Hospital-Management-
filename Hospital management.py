 ## First Connect to database and select database

 ## Then print "WELCOME TO HOSPITAL MANAGEMENT SYSTEM"

 ## After then print
 ## PRESS 1: PATIENTS MANAGEMENT
 ## PRESS 2: DOCTOR MANAGEMENT
 ## PRESS 3: TAKE AN APPOINTMENT
 ## PRESS 4: BREAK

 ## ------PRESS 1: PATIENTS MANAGEMENT ------
 ## print and PRESS 1: REGISTER A NEW PATIENT
 ## PRESS 2: UPDATE PATIENT
 ## PRESS 3: REMOVE PATIENT
 ## PRESS 4: SEARCH PATIENT DETAILS
 ## PRESS 5: DISPLAY ALL PATIENTS RECORDS
 ## PRESS 6: BREAK

 ## ------PRESS 2: DOCTORS MANAGEMENT--------
 ## print and PRESS 1: REGISTER A NEW DOCTOR
 ## PRESS 2: UPDATE DOCTOR
 ## PRESS 3: REMOVE DOCTOR
 ## PRESS 4: SEARCH DOCTOR DETAILS
 ## PRESS 5: DISPLAY ALL DOCTORS RECORDS
 ## PRESS 6: BREAK

 ## ------PRESS 3: TAKE AN APPOINTMENT-------


"""CONNECT TO DATABASE"""
import mysql.connector as m
mydb=m.connect(host="localhost",user="root",passwd="root")
if mydb.is_connected():
    print("Connection successfull")
    cur=mydb.cursor()

"""CREATE DATABASE"""
cur.execute("create database HOSPITAL_MANAGEMENT_SYSTEM")

"""SELECT DATABASE"""
cur.execute("use HOSPITAL_MANAGEMENT_SYSTEM")

"""CREATE A TABLE"""
cur.execute("create table PATIENTS (Patient_ID int, Name varchar(20), Sex\
varchar(1), Age int, Contact_No varchar(20),\
 Address varchar(30), Father_Name varchar(20),\
Date_of_registration varchar(20))")

cur.execute("create table DOCTORS (DOCTOR_ID int, Name varchar(20), Sex\
varchar(1), Age int, Contact_No varchar(20),\
Address varchar(30), Qualification varchar(20),\
Date_of_Joining varchar(20))")

cur.execute("create table APPOINTMENTS (Name varchar(20), Sex varchar(1),\
Age int, Date_of_registration varchar(20),\
Problem varchar(30))")



"""PROGRAM"""

def PATIENTS_MANAGEMENT():
    
    def PATIENT_REGISTRATION():
        Patient_ID=int(input("Enter Patient ID: "))
        Name=input("Enter Patient Name: ")
        Sex=input("Enter Sex of Patient(M/F/O): ")
        Age=int(input("Enter Patient Age: "))
        Contact_No=input("Enter Patient Contact Number: ")
        Address=input("Enter Patient Address: ")
        Father_Name=input("Enter Patient Father Name: ")
        Date_of_registration=input("Enter Date of Registration: ")
        Syntax="insert into PATIENTS
        values('%d','%s','%s','%d','%s','%s','%s','%s')"%\
        (Patient_ID, Name, Sex, Age, Contact_No,\
        Address,Father_Name,Date_of_registration)
        cur.execute(Syntax)
        mydb.commit()
        print("Patient record successfully inserted!!")
    
    def PATIENT_UPDATE():
        Patient_ID=int(input("Enter Patient ID whose records you wish to update: "))
        Name=input("Enter modified Patient Name: ")
        Sex=input("Enter correct Sex of Patient(M/F/O): ")
        Age=int(input("Enter correct Patient Age: "))
        Contact_No=input("Enter modified Patient Contact Number: ")
        Address=input("Enter new Patient Address: ")
        Father_Name=input("Enter modified Father Name: ")
        Date_of_registration=input("Enter correct Date of Registration:")
        Syntax="update PATIENTS set Patient_ID='%d', Name='%s', Sex='%s',
        Age='%d', Contact_No='%s', Address='%s',\
        Father_Name='%s',Date_of_registration='%s'"\
        %(Patient_ID, Name, Sex, Age, Contact_No,Address,Father_Name,Date_of_registration)
        cur.execute(Syntax)
        print("Patient Record Updated Successfully!!")
    
    def PATIENT_DELETE():
        PID=input("Enter Patient ID whose record you want to delete: ")
        Syntax="delete from PATIENTS where Patient_ID=%s" %(PID)
        try:
            cur.execute(Syntax)
            print("Patient Record Successfully Deleted!!")
        except:
            print("Invalid Patient ID!!")
    
    def PATIENT_SEARCH():
        PID=input("Enter Patient ID whose record you want to search: ")
        try:
            Syntax="Select * from PATIENTS where Patient_ID=%s" %(PID)
            cur.execute(Syntax)
            record=cur.fetchall()
            for i in record:
                print("Record of the patient",PID)
                print(i)
        except:
            print("Invalid Patient ID!!")
    
    def PATIENT_DISPLAY():
        try:
            Syntax="Select * from PATIENTS"
            cur.execute(Syntax)
            record=cur.fetchall()
            for i in record:
                print("Details of the patients are:")
                print(i)
        except:
            print("No record found")

while True:
    print(" ")
    print("...................................................................")
    print(" <<<<<< PATIENT MENU >>>>>>")
    print(" PRESS 1: TO REGISTER A NEW PATIENT")
    print(" PRESS 2: TO UPDATE EXISTING PATIENT RECORD")
    print(" PRESS 3: TO REMOVE PATIENT RECORD")
    print(" PRESS 4: TO SEARCH FOR A PATIENT RECORD")
    print(" PRESS 5: TO DISPLAY ALL PATIENTS RECORDS")
    print(" PRESS 6: EXIT")
    print("...................................................................")
    Option=int(input("Enter the option number you wish to implement:"))
    if Option==1:
        PATIENT_REGISTRATION()
    elif Option==2:
        PATIENT_UPDATE()
    elif Option==3:
        PATIENT_DELETE()
    elif Option==4:
        PATIENT_SEARCH()
    elif Option==5:
        PATIENT_DISPLAY()
    elif Option==6:
        print("HAVE A NICE DAY!")
        break
    else:
        print("Please provide valid choice!!")


def DOCTORS_MANAGEMENT():
    
    def DOCTOR_REGISTRATION():
        Doctor_ID=int(input("Enter Doctor ID: "))
        Name=input("Enter Doctor Name: ")
        Sex=input("Enter Sex of Doctor(M/F/O): ")
        Age=int(input("Enter Doctor Age: "))
        Contact_No=input("Enter Doctor Contact Number: ")
        Address=input("Enter Doctor Address: ")
        Qualification=input("Enter Doctor's qualification: ")
        Date_of_Joining=input("Enter Date of joining: ")
        Syntax="insert into DOCTOR"
        values('%d','%s','%s','%d','%s','%s','%s','%s')"%\
        (Doctor_ID, Name, Sex, Age, Contact_No, Address,\
        Qualification, Date_of_Joining)
        cur.execute(Syntax)
        mydb.commit()
        print("Doctor record successfully inserted!!")
    
    def DOCTOR_UPDATE():
        Doctor_ID=int(input("Enter Doctor ID whose records you wish to update: "))
        Name=input("Enter modified Doctor Name: ")
        Sex=input("Enter correct Sex of Doctor(M/F/O): ")
        Age=int(input("Enter correct Doctor Age: "))
        Contact_No=input("Enter modified Doctor Contact Number: ")
        Address=input("Enter new Doctor Address: ")
        Qualification=input("Enter modified Qualification: ")
        Date_of_Joining=input("Enter correct Date of Joining: ")
        Syntax="update DOCTORS set Doctor_ID='%d', Name='%s', Sex='%s',
        Age='%d', Contact_No='%s', Address='%s',\
        Qualification='%s',Date_of_Joining='%s'"\
        %(Doctor_ID, Name, Sex, Age, Contact_No, Address,\
        Qualification, Date_of_Joining)
        cur.execute(Syntax)
        print("Doctor Record Updated Successfully!!")
    
    def DOCTOR_DELETE():
        DID=input("Enter Doctor ID whose record you want to delete: ")
        Syntax="delete from DOCTORS where Doctor_ID=%s" %(DID)
        try:
            cur.execute(Syntax)
            print("Doctor Record Successfully Deleted!!")
        except:
            print("Invalid Doctor ID!!")
    
    def DOCTOR_SEARCH():
        DID=input("Enter Doctor ID whose record you want to search: ")
        try:
            Syntax="Select * from DOCTORS where Doctor_ID=%s" %(DID)
            cur.execute(Syntax)
            record=cur.fetchall()
            for i in record:
                print("Record of the Doctor",DID)
                print(i)
        except:
            print("Invalid Doctor ID!!")

    def DOCTOR_DISPLAY():
        try:
            Syntax="Select * from DOCTORS"
            cur.execute(Syntax)
            record=cur.fetchall()
            for i in record:
                print("Details of the Doctors are:")
                print(i)
        except:
            print("No record found")

while True:
    print(" ")
    print("...................................................................")
    print(" <<<<<< DOCTOR MENU >>>>>>")
    print(" PRESS 1: TO REGISTER A NEW DOCTOR")
    print(" PRESS 2: TO UPDATE EXISTING DOCTOR RECORD")
    print(" PRESS 3: TO REMOVE DOCTOR RECORD")
    print(" PRESS 4: TO SEARCH FOR A DOCTOR RECORD")
    print(" PRESS 5: TO DISPLAY ALL DOCTORS RECORDS")
    print(" PRESS 6: EXIT")
    print("...................................................................")
    Option=int(input("Enter the option number you wish to implement:"))
    if Option==1:
        DOCTOR_REGISTRATION()
    elif Option==2:
        DOCTOR_UPDATE()
    elif Option==3:
        DOCTOR_DELETE()
    elif Option==4:
        DOCTOR_SEARCH()
    elif Option==5:
        DOCTOR_DISPLAY()
    elif Option==6:
        print("HAVE A NICE DAY!")
        break
    else:
        print("Please provide valid choice!!")


def TAKE_APPOINTMENT():
    Patient_Name=input("Enter patient's name")
    Sex=input("Enter sex of patient(M/F/O): ")
    Age=int(input("Enter patient age: "))
    Date_of_registration=input("Enter Date of Registration: ")
    Problem=input("Enter your's problem: ")
    Syntax="insert into APPOINTMENTS values('%s','%s','%d','%s','%s')"%\
    (Patient_Name, Sex, Age, Date_of_registration, Problem)
    cur.execute(Syntax)
    mydb.commit()
    print("You have successfully taken appointment!!")
    print("Thanks")

"""MAIN MENU"""
while True:
    print(" ")
    print("______________________CITY HOSPITAL NEW DELHI_____________________")
    print("_______________WELCOME TO HOSPITAL MANAGEMENT SYSTEM______________")
    print(" ")
    print("...................................................................")
    print(" <<<<<< MAIN MENU >>>>>>")
    print(" PRESS 1: PATIENTS MANAGEMENT")
    print(" PRESS 2: DOCTORS MANAGEMENT")
    print(" PRESS 3: TAKE AN APPOINTMENT")
    print(" PRESS 4: EXIT")
    print("...................................................................")
    option=int(input("Enter the option number you wish to implement: "))
    if Option==1:
        PATIENTS_MANAGEMENT()
    elif Option==2:
        DOCTORS_MANAGEMENT()
    elif Option==3:
        TAKE_APPOINTMENT()
    elif Option==4:
        print("........THANKYOU FOR USING OUR PROGRAM........")
        print(" HAVE A NICE DAY!")
        break
    else:
        print("Please provide valid choice!!")



Connection successfull

______________________CITY HOSPITAL NEW DELHI_____________________
_______________WELCOME TO HOSPITAL MANAGEMENT SYSTEM______________

...................................................................
 <<<<<< MAIN MENU >>>>>>
 PRESS 1: PATIENTS MANAGEMENT
 PRESS 2: DOCTORS MANAGEMENT
 PRESS 3: TAKE AN APPOINTMENT
 PRESS 4: EXIT
...................................................................
Enter the option number you wish to implement: 1

...................................................................
 <<<<<< PATIENT MENU >>>>>>
 PRESS 1: TO REGISTER A NEW PATIENT
 PRESS 2: TO UPDATE EXISTING PATIENT RECORD
 PRESS 3: TO REMOVE PATIENT RECORD
 PRESS 4: TO SEARCH FOR A PATIENT RECORD
 PRESS 5: TO DISPLAY ALL PATIENTS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 1
Enter Patient ID: 1001
Enter Patient Name: Siya
Enter Sex of Patient(M/F/O): F
Enter Patient Age: 25
Enter Patient Contact Number: 6859504958
Enter Patient Address: Mehrauli
Enter Patient Father Name: Jadish
Enter Date of Registration: 2022-02-12
Patient record successfully inserted!!

...................................................................
 <<<<<< PATIENT MENU >>>>>>
 PRESS 1: TO REGISTER A NEW PATIENT
 PRESS 2: TO UPDATE EXISTING PATIENT RECORD
 PRESS 3: TO REMOVE PATIENT RECORD
 PRESS 4: TO SEARCH FOR A PATIENT RECORD
 PRESS 5: TO DISPLAY ALL PATIENTS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 2
Enter Patient ID whose records you wish to update: 1001
Enter modified Patient Name: Siya
Enter correct Sex of Patient(M/F/O): F
Enter correct Patient Age: 25
Enter modified Patient Contact Number: 6859504958
Enter new Patient Address: Mehrauli
Enter modified Father Name: Jadish
Enter correct Date of Registration: 2022-02-12
Patient Record Updated Successfully!!

...................................................................
 <<<<<< PATIENT MENU >>>>>>
 PRESS 1: TO REGISTER A NEW PATIENT
 PRESS 2: TO UPDATE EXISTING PATIENT RECORD
 PRESS 3: TO REMOVE PATIENT RECORD
 PRESS 4: TO SEARCH FOR A PATIENT RECORD
 PRESS 5: TO DISPLAY ALL PATIENTS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 4
Enter Patient ID whose record you want to search: 1001
Record of the patient 1001
(1001, 'Siya', 'F', 25, '6859504958', 'Mehrauli', 'Jadish', '2022-02-12')

...................................................................
 <<<<<< PATIENT MENU >>>>>>
 PRESS 1: TO REGISTER A NEW PATIENT
 PRESS 2: TO UPDATE EXISTING PATIENT RECORD
 PRESS 3: TO REMOVE PATIENT RECORD
 PRESS 4: TO SEARCH FOR A PATIENT RECORD
 PRESS 5: TO DISPLAY ALL PATIENTS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 5
Details of the patients are:
(1001, 'Siya', 'F', 25, '6859504958', 'Mehrauli', 'Jadish', '2022-02-12')

...................................................................
 <<<<<< PATIENT MENU >>>>>>
 PRESS 1: TO REGISTER A NEW PATIENT
 PRESS 2: TO UPDATE EXISTING PATIENT RECORD
 PRESS 3: TO REMOVE PATIENT RECORD
 PRESS 4: TO SEARCH FOR A PATIENT RECORD
 PRESS 5: TO DISPLAY ALL PATIENTS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 3
Enter Patient ID whose record you want to delete: 1001
Patient Record Successfully Deleted!!

...................................................................
 <<<<<< PATIENT MENU >>>>>>
 PRESS 1: TO REGISTER A NEW PATIENT
 PRESS 2: TO UPDATE EXISTING PATIENT RECORD
 PRESS 3: TO REMOVE PATIENT RECORD
 PRESS 4: TO SEARCH FOR A PATIENT RECORD
 PRESS 5: TO DISPLAY ALL PATIENTS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 6
HAVE A NICE DAY!

______________________CITY HOSPITAL NEW DELHI_____________________
_______________WELCOME TO HOSPITAL MANAGEMENT SYSTEM______________

...................................................................
 <<<<<< MAIN MENU >>>>>>
 PRESS 1: PATIENTS MANAGEMENT
 PRESS 2: DOCTORS MANAGEMENT
 PRESS 3: TAKE AN APPOINTMENT
 PRESS 4: EXIT
...................................................................
Enter the option number you wish to implement: 2

...................................................................
 <<<<<< DOCTOR MENU >>>>>>
 PRESS 1: TO REGISTER A NEW DOCTOR
 PRESS 2: TO UPDATE EXISTING DOCTOR RECORD
 PRESS 3: TO REMOVE DOCTOR RECORD
 PRESS 4: TO SEARCH FOR A DOCTOR RECORD
 PRESS 5: TO DISPLAY ALL DOCTORS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 1
Enter Doctor ID: 1001
Enter Doctor Name: Danushree
Enter Sex of Doctor(M/F/O): F
Enter Doctor Age: 45
Enter Doctor Contact Number: 8908908900
Enter Doctor Address: Mehrauli
Enter Doctor's qualification: MBBS, MD
Enter Date of joining: 2006-02-12
Doctor record successfully inserted!!

...................................................................
 <<<<<< DOCTOR MENU >>>>>>
 PRESS 1: TO REGISTER A NEW DOCTOR
 PRESS 2: TO UPDATE EXISTING DOCTOR RECORD
 PRESS 3: TO REMOVE DOCTOR RECORD
 PRESS 4: TO SEARCH FOR A DOCTOR RECORD
 PRESS 5: TO DISPLAY ALL DOCTORS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 2
Enter Doctor ID whose records you wish to update: 1001
Enter modified Doctor Name: Danushree
Enter correct Sex of Doctor(M/F/O): F
Enter correct Doctor Age: 45
Enter modified Doctor Contact Number: 8908908900
Enter new Doctor Address: Mehrauli
Enter modified Qualification: MBBS, MD
Enter correct Date of Joining: 2006-02-12
Doctor Record Updated Successfully!!

...................................................................
 <<<<<< DOCTOR MENU >>>>>>
 PRESS 1: TO REGISTER A NEW DOCTOR
 PRESS 2: TO UPDATE EXISTING DOCTOR RECORD
 PRESS 3: TO REMOVE DOCTOR RECORD
 PRESS 4: TO SEARCH FOR A DOCTOR RECORD
 PRESS 5: TO DISPLAY ALL DOCTORS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 4
Enter Doctor ID whose record you want to search: 1001
Record of the Doctor 1001
(1001, 'Danushree', 'F', 45, '8908908900', 'Mehrauli', 'MBBS, MD', '2006-
02-12')

...................................................................
 <<<<<< DOCTOR MENU >>>>>>
 PRESS 1: TO REGISTER A NEW DOCTOR
 PRESS 2: TO UPDATE EXISTING DOCTOR RECORD
 PRESS 3: TO REMOVE DOCTOR RECORD
 PRESS 4: TO SEARCH FOR A DOCTOR RECORD
 PRESS 5: TO DISPLAY ALL DOCTORS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 5
Details of the Doctors are:
(1001, 'Danushree', 'F', 45, '8908908900', 'Mehrauli', 'MBBS, MD', '2006-
02-12')

...................................................................
 <<<<<< DOCTOR MENU >>>>>>
 PRESS 1: TO REGISTER A NEW DOCTOR
 PRESS 2: TO UPDATE EXISTING DOCTOR RECORD
 PRESS 3: TO REMOVE DOCTOR RECORD
 PRESS 4: TO SEARCH FOR A DOCTOR RECORD
 PRESS 5: TO DISPLAY ALL DOCTORS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 3
Enter Doctor ID whose record you want to delete: 1001
Doctor Record Successfully Deleted!!

...................................................................
 <<<<<< DOCTOR MENU >>>>>>
 PRESS 1: TO REGISTER A NEW DOCTOR
 PRESS 2: TO UPDATE EXISTING DOCTOR RECORD
 PRESS 3: TO REMOVE DOCTOR RECORD
 PRESS 4: TO SEARCH FOR A DOCTOR RECORD
 PRESS 5: TO DISPLAY ALL DOCTORS RECORDS
 PRESS 6: EXIT
...................................................................
Enter the option number you wish to implement: 6
HAVE A NICE DAY!

______________________CITY HOSPITAL NEW DELHI_____________________
_______________WELCOME TO HOSPITAL MANAGEMENT SYSTEM______________

...................................................................
 <<<<<< MAIN MENU >>>>>>
 PRESS 1: PATIENTS MANAGEMENT
 PRESS 2: DOCTORS MANAGEMENT
 PRESS 3: TAKE AN APPOINTMENT
 PRESS 4: EXIT
...................................................................
Enter the option number you wish to implement: 3
Enter patient's nameSiya
Enter sex of patient(M/F/O): F
Enter patient age: 25
Enter Date of Registration: 2002-02-12
Enter your's problem: Toothache
You have successfully taken appointment!!
Thanks

______________________CITY HOSPITAL NEW DELHI_____________________
_______________WELCOME TO HOSPITAL MANAGEMENT SYSTEM______________

...................................................................
 <<<<<< MAIN MENU >>>>>>
 PRESS 1: PATIENTS MANAGEMENT
 PRESS 2: DOCTORS MANAGEMENT
 PRESS 3: TAKE AN APPOINTMENT
 PRESS 4: EXIT
...................................................................
Enter the option number you wish to implement: 4
........THANKYOU FOR USING OUR PROGRAM........
 HAVE A NICE DAY! 