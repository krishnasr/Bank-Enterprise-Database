CREATE TABLE Branch ( Branch_name VARCHAR(20) NOT NULL,
			Branch_city VARCHAR(20),
			Assests VARCHAR(20),
			PRIMARY KEY (Branch_name));

CREATE TABLE Employee ( Emp_ssn INT NOT NULL,
			Emp_name VARCHAR(20),
			Emp_telephone INT,
			Startdate DATE,
			Emp_manag_ssn INT,
			PRIMARY KEY (Emp_ssn));

ALTER TABLE Employee ADD FOREIGN KEY (Emp_manag_ssn) REFERENCES Employee (Emp_ssn) ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE Customer ( Cust_ssn INT NOT NULL,
			Cust_name VARCHAR(20),
			Cust_street VARCHAR(30),
			Cust_city VARCHAR(20),
			Type VARCHAR(15),
			Emp_ssn INT,
			PRIMARY KEY (Cust_ssn),
			FOREIGN KEY (Emp_ssn) REFERENCES Employee (Emp_ssn) ON DELETE CASCADE ON UPDATE CASCADE);


CREATE TABLE Loan ( Loan_no INT NOT NULL,
			Loan_amount DECIMAL(10,2),
			Branch_name VARCHAR(20),
			PRIMARY KEY (Loan_no),
			FOREIGN KEY (Branch_name) REFERENCES Branch (Branch_name) ON DELETE CASCADE ON UPDATE CASCADE);
			

CREATE TABLE Payment ( Loan_no INT NOT NULL,
			Pay_no INT NOT NULL,
			Pay_date DATE,
			Pay_amount DECIMAL(10,2),
			PRIMARY KEY(Loan_no,Pay_no),
			FOREIGN KEY (Loan_no) REFERENCES Loan (Loan_no) ON DELETE CASCADE ON UPDATE CASCADE);


CREATE TABLE Borrower ( Loan_no INT NOT NULL,
			Cust_ssn INT NOT NULL,
			PRIMARY KEY(Loan_no,Cust_ssn),
			FOREIGN KEY (Loan_no) REFERENCES Loan (Loan_no) ON DELETE CASCADE ON UPDATE CASCADE,
			FOREIGN KEY (Cust_ssn) REFERENCES Customer (Cust_ssn) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Depname ( Emp_ssn INT NOT NULL,
			Emp_depname VARCHAR(20) NOT NULL,
			PRIMARY KEY (Emp_ssn, Emp_depname),
			FOREIGN KEY (Emp_ssn) REFERENCES Employee(Emp_ssn) ON DELETE CASCADE ON UPDATE CASCADE);


CREATE TABLE Account ( Account_no INT NOT NULL,
			Balance DECIMAL(10,2),
			Deposit DECIMAL (10,2),
			Withdrawal DECIMAL(10,2),
			PRIMARY KEY(Account_no));

CREATE TABLE Savings_acc ( Account_no INT NOT NULL,
				Interest_rate INT,
				PRIMARY KEY (Account_no),
				FOREIGN KEY(Account_no) REFERENCES Account(Account_no) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE Checking_acc ( Account_no INT NOT NULL,
				Overdrafts VARCHAR(20),
				PRIMARY KEY (Account_no),
				FOREIGN KEY(Account_no) REFERENCES Account(Account_no) ON DELETE CASCADE ON UPDATE CASCADE);
				
CREATE TABLE Depositor (Account_no INT NOT NULL,
			Cust_ssn INT NOT NULL,
			Date_accessed DATE,
			PRIMARY KEY (Account_no, Cust_ssn),
			FOREIGN KEY (Account_no) REFERENCES Account(Account_no) ON DELETE CASCADE ON UPDATE CASCADE,
			FOREIGN KEY (Cust_ssn) REFERENCES Customer (Cust_ssn) ON DELETE CASCADE ON UPDATE CASCADE);
			 