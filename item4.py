from os import access
import pandas as pd

import mysql.connector as mesql
from mysql.connector import Error
try:
    connet=mesql.connect(host="acadmysqldb001p.uta.edu",user="kxs0344",password="Scarenage@0512")
    if connet.is_connected():
        cursor=connet.cursor()
        print("Database is connected")
        cursor.execute("USE kxs0344;")
        print("4.1 adding new customer who is a borrower as well as a depositor")
        branchno=str(input("enter the Branch name: "))
        branchno="'"+branchno+"'"
        cust_ssn=str(input("enter the customer ssn: "))
        cust_name=str(input("enter Customer Name: "))
        cust_name="'"+cust_name+"'"
        cust_street=str(input("enter street: "))
        cust_street="'"+cust_street+"'"
        cust_city=str(input("enter city: "))
        cust_city="'"+cust_city+"'"
        type1=str(input("enter the banking type: "))
        type1="'"+type1+"'"
        account_no=str(input("enter account number: "))
        accessingdate=str(input("enter date: "))
        accessingdate="'"+accessingdate+"'"
        loanno=str(input("enter loan number:"))
        emp_ssn=str(input("enter the emp: "))
        cursor.execute("INSERT INTO Customer values("+cust_ssn+","+cust_name+","+cust_street+","+cust_city+","+type1+","+emp_ssn+");")
        cursor.execute("INSERT INTO Loan values("+loanno+",1000.00,"+branchno+");")
        cursor.execute("INSERT INTO Borrower values("+loanno+","+cust_ssn+");")
        cursor.execute("INSERT INTO Account values("+account_no+",100.00,0.00,0.00);")
        cursor.execute("INSERT INTO Depositor values("+account_no+","+cust_ssn+","+accessingdate+");")
        print("4.2 new customer loan details added")
        print("4.3 add new Employee who is manager")
        emp_ssn1=str(input("enter the new Employee ssn: "))
        emp_name=str(input("enter Employee Name : "))
        emp_name="'"+emp_name+"'"
        emp_telephone=str(input("enter the new Employee telephone number : "))
        startdate=str(input("enter starting date: "))
        startdate="'"+startdate+"'"
        cursor.execute("INSERT INTO Employee values("+emp_ssn1+","+emp_name+","+emp_telephone+","+startdate+","+emp_ssn1+");")
        cursor.execute("update Employee set Emp_manag_ssn=NULL where Emp_ssn="+emp_ssn1+";")
        print("4.4 Loan payment transactions")
        Loan_no1=str(input("enter Loan number: "))
        pay_no=str(input("enter payment number: "))
        paydate=str(input("enter payment date: "))
        paydate="'"+paydate+"'"
        pay_amount=str(input("enter payment amount: "))
        cursor.execute("INSERT INTO Payment values("+Loan_no1+","+pay_no+","+paydate+","+pay_amount+");")
        cursor.execute("update Loan set Loan_amount=Loan_amount-"+pay_amount+ " where Loan_no="+Loan_no1+";" )
        print("4.5 new savings account for the customer")
        if type1=="savings":
            interestrate=str(input("enter interest rate for the new savings account: "))
            cursor.execute("INSERT INTO Savings_acc values("+account_no+","+interestrate+");")
        print("4.6 open new branch for the bank")
        branchname=str(input("enter new branch name: "))
        branchname="'"+branchname+"'"
        branchcity=str(input("enter new branch city: "))
        branchcity="'"+branchcity+"'"
        assests=str(input("enter new branch assets: "))
        assests="'"+assests+"'"
        cursor.execute("INSERT INTO Branch values("+branchname+","+branchcity+","+assests+");")

        
        connet.commit()

except Error as err:
    print("Error while connecting to mysql",err)
