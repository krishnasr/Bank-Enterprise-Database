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
        cursor.execute("SELECT * FROM Customer;")
        customer=cursor.fetchall()
        cursor.execute("SELECT * FROM Loan;")
        loan=cursor.fetchall()
        cursor.execute("select * from Borrower;")
        borrower=cursor.fetchall()
        loan=pd.DataFrame(loan,columns=['Loan_no','Loan_amount','branch_name'])
        customer=pd.DataFrame(customer,columns=['Cust_ssn','Cust_name','Cust_street','Cust_city','type','Emp_ssn'])
        result5=customer.join(loan)
        print(result5)
        
        

        


        
        


        
        connet.commit()

except Error as err:
    print("Error while connecting to mysql",err)
