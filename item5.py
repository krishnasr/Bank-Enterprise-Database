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
        cursor.execute("SELECT * FROM Loan;")
        loan=cursor.fetchall()
        cursor.execute("select * from Account;")
        account=cursor.fetchall()
        cursor.execute("select * from Savings_acc;")
        savings=cursor.fetchall()
        cursor.execute("select * from Checking_acc;")
        checking=cursor.fetchall()
        loan=pd.DataFrame(loan,columns=['Loan_no','Total_Balance','Branch_name'])
        account=pd.DataFrame(account,columns=['Account_no','Balance','Deposit','Withdrawal'])
        savings=pd.DataFrame(savings,columns=['Saving_acc_no','Interestrate'])
        checking=pd.DataFrame(checking,columns=['Checking_acc_no','overdraft'])
        result=loan.join(account)
        result=result.join(savings)
        result5=result.join(checking)
        print(result5)
        
        

        


        
        


        
        connet.commit()

except Error as err:
    print("Error while connecting to mysql",err)
