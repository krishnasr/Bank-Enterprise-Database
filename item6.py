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
        cursor1=("CREATE TRIGGER execeed BEFORE INSERT  ON Account FOR EACH ROW BEGIN IF (Account.Withdrawal > (select Overdrafts from Checking_acc)) THEN PRINT 'ERROR';")
        accountno=input(str("enter account no: "))
        balance=input(str("enter balance: "))
        deposit=input(str("enter deposit: "))
        withdraw=input(str("enter withdrawal: "))
        overdraft=input(str("enter overdraft: "))
        if int(balance)<=0:
            if int (withdraw)>int(overdraft):
                print("!!!overdraft limit execeeded!!!")
        else:
            cursor.execute("INSERT INTO Account values("+accountno+","+balance+","+deposit+","+withdraw+");")
            cursor.execute("INSERT INTO Checking_acc values("+accountno+","+overdraft+");")
        cursor.execute("SELECT Emp_ssn, Startdate CASE WHEN YEAR(Startdate)<2012 THEN '10 year Anniversary' END AS Anniversary FROM Employee;")
        cursor2=("CREATE TRIGGER anniversary BEFORE INSERT ON Employee FOR EACH ROW BEGIN IF Startdate > 3650 THEN alert(' 10th Anniversary') END IF END; ")

except Error as err:
    print("Error while connecting to mysql",err)
