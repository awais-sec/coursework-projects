-- Create Shop managment system Database 
CREATE DATABASE ComputerShopManagmentSystem 

-- Create Customer table
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    CustomerName NVARCHAR(50),
    CustomerAddress NVARCHAR(100),
    CustomerPhoneNo NVARCHAR(15),
    CustomerBalance DECIMAL(15, 2)
);

-- Insert values into Customer table
INSERT INTO Customer (CustomerID, CustomerName, CustomerAddress, CustomerPhoneNo, CustomerBalance)
VALUES
    (1, 'Ali Khan', 'House No. 123, Street 1, Lahore', '03001234567', 10000.00),
    (2, 'Sana Ahmed', 'Flat No. 456, Street 2, Karachi', '03111234567', 15000.00),
    (3, 'Ahmed Hassan', 'Apartment No. 789, Street 3, Islamabad', '03221234567', 20000.00),
    (4, 'Fatima Malik', 'House No. 987, Street 4, Rawalpindi', '03331234567', 25000.00),
    (5, 'Imran Khan', 'House No. 654, Street 5, Faisalabad', '03441234567', 30000.00),
    (6, 'Ayesha Khan', 'House No. 321, Street 6, Multan', '03551234567', 35000.00),
    (7, 'Hamza Ali', 'Flat No. 876, Street 7, Peshawar', '03661234567', 40000.00),
    (8, 'Sadia Ahmed', 'Apartment No. 543, Street 8, Quetta', '03771234567', 45000.00),
    (9, 'Zainab Hassan', 'House No. 210, Street 9, Gujranwala', '03881234567', 50000.00),
    (10, 'Bilal Malik', 'House No. 987, Street 10, Sialkot', '03991234567', 55000.00),
    (11, 'Zoya Khan', 'House No. 654, Street 11, Hyderabad', '03011234568', 60000.00),
    (12, 'Usman Ali', 'Flat No. 321, Street 12, Sukkur', '03121234568', 65000.00),
    (13, 'Hina Ahmed', 'House No. 876, Street 13, Larkana', '03231234568', 70000.00),
    (14, 'Kamran Hassan', 'House No. 543, Street 14, Nawabshah', '03341234568', 75000.00),
    (15, 'Sara Malik', 'Flat No. 210, Street 15, Mirpur Khas', '03451234568', 80000.00);

-- Create Balance table
CREATE TABLE Balance (
    InvoiceNo INT PRIMARY KEY,
    CustomerID INT FOREIGN KEY REFERENCES Customer(CustomerID),
    PaidAmount DECIMAL(8, 2),
    TotalAmount DECIMAL(8, 2),
    Dat DATE
);

-- Insert values into Balance table
INSERT INTO Balance (InvoiceNo, CustomerID, PaidAmount, TotalAmount, Dat)
VALUES
    (1, 1, 100.00, 150.00, '2024-02-08'),
    (2, 2, 200.00, 250.00, '2024-02-08'),
    (3, 3, 300.00, 350.00, '2024-02-08'),
    (4, 4, 400.00, 450.00, '2024-02-08'),
    (5, 5, 500.00, 550.00, '2024-02-08'),
    (6, 6, 600.00, 650.00, '2024-02-08'),
    (7, 7, 700.00, 750.00, '2024-02-08'),
    (8, 8, 800.00, 850.00, '2024-02-08'),
    (9, 9, 900.00, 950.00, '2024-02-08'),
    (10, 10, 1000.00, 1050.00, '2024-02-08'),
    (11, 11, 1100.00, 1150.00, '2024-02-08'),
    (12, 12, 1200.00, 1250.00, '2024-02-08'),
    (13, 13, 1300.00, 1350.00, '2024-02-08'),
    (14, 14, 1400.00, 1450.00, '2024-02-08'),
    (15, 15, 1500.00, 1550.00, '2024-02-08');

-- Create ComputerPartDetail table
CREATE TABLE ComputerPartDetail (
    SerialNo NVARCHAR(10) PRIMARY KEY,
    ItemName NVARCHAR(50),
    BrandName NVARCHAR(50),
    Typ NVARCHAR(10),
    Price DECIMAL(7, 2),
    Warranty INT
);
-- Inserting values in ComputerPartDetail table
INSERT INTO ComputerPartDetail (SerialNo, ItemName, BrandName, Typ, Price, Warranty)
VALUES
    ('SER001', 'Item 1', 'Brand A', 'Type1', 100.00, 1),
    ('SER002', 'Item 2', 'Brand B', 'Type2', 200.00, 2),
    ('SER003', 'Item 3', 'Brand C', 'Type3', 300.00, 3),
    ('SER004', 'Item 4', 'Brand D', 'Type4', 400.00, 4),
    ('SER005', 'Item 5', 'Brand E', 'Type5', 500.00, 5),
    ('SER006', 'Item 6', 'Brand F', 'Type6', 600.00, 6),
    ('SER007', 'Item 7', 'Brand G', 'Type7', 700.00, 7),
    ('SER008', 'Item 8', 'Brand H', 'Type8', 800.00, 8),
    ('SER009', 'Item 9', 'Brand I', 'Type9', 900.00, 9),
    ('SER010', 'Item 10', 'Brand J', 'Type10', 1000.00, 10),
    ('SER011', 'Item 11', 'Brand K', 'Type11', 1100.00, 11),
    ('SER012', 'Item 12', 'Brand L', 'Type12', 1200.00, 12),
    ('SER013', 'Item 13', 'Brand M', 'Type13', 1300.00, 13),
    ('SER014', 'Item 14', 'Brand N', 'Type14', 1400.00, 14),
    ('SER015', 'Item 15', 'Brand O', 'Type15', 1500.00, 15);



--Create ComputerSystemDetail table
CREATE TABLE ComputerSystemDetail (
    ModelNo NVARCHAR(25) PRIMARY KEY,
    SystemName NVARCHAR(25),
    BrandName NVARCHAR(25),
    Category NVARCHAR(25),
    Price DECIMAL(10, 2),
    Warranty INT,
    Ram NVARCHAR(8),
    Motherboard NVARCHAR(50),
    Monitor NVARCHAR(50),
    Processor NVARCHAR(50),
    OtherDescription NVARCHAR(100)
); 
--Inserting values in ComputerSystemDetail table
INSERT INTO ComputerSystemDetail (ModelNo, SystemName, BrandName, Category, Price, Warranty, Ram, Motherboard, Monitor, Processor, OtherDescription)
VALUES
    ('MOD001', 'System 1', 'Brand A', 'Desktop', 1500.00, 1, '8GB', 'Intel H310', '21" LED', 'Intel Core i5', 'Includes keyboard and mouse'),
    ('MOD002', 'System 2', 'Brand B', 'Laptop', 2000.00, 1, '16GB', 'AMD B450', '15.6" LCD', 'AMD Ryzen 7', 'Includes webcam and microphone'),
    ('MOD003', 'System 3', 'Brand C', 'Desktop', 1800.00, 1, '12GB', 'ASUS PRIME B450M', '23" LED', 'AMD Ryzen 5', 'Includes Wi-Fi adapter'),
    ('MOD004', 'System 4', 'Brand D', 'Laptop', 2500.00, 1, '8GB', 'GIGABYTE B450 AORUS M', '14" OLED', 'Intel Core i7', 'Includes carrying case'),
    ('MOD005', 'System 5', 'Brand E', 'Desktop', 1600.00, 1, '16GB', 'MSI B450 TOMAHAWK', '24" LED', 'AMD Ryzen 7', 'Includes wireless keyboard and mouse'),
    ('MOD006', 'System 6', 'Brand F', 'Laptop', 2200.00, 1, '8GB', 'MSI B450I GAMING PLUS AC', '13.3" LCD', 'Intel Core i5', 'Includes external DVD drive'),
    ('MOD007', 'System 7', 'Brand G', 'Desktop', 1900.00, 1, '8GB', 'ASRock B450M PRO4', '27" LED', 'AMD Ryzen 5', 'Includes HDMI cable'),
    ('MOD008', 'System 8', 'Brand H', 'Laptop', 2700.00, 1, '16GB', 'GIGABYTE B450M DS3H', '17" LCD', 'AMD Ryzen 7', 'Includes laptop bag'),
    ('MOD009', 'System 9', 'Brand I', 'Desktop', 1750.00, 1, '12GB', 'GIGABYTE B450 AORUS ELITE', '22" LED', 'Intel Core i7', 'Includes gaming headset'),
    ('MOD010', 'System 10', 'Brand J', 'Laptop', 2400.00, 1, '8GB', 'ASUS ROG Strix B450-F', '15.6" OLED', 'AMD Ryzen 5', 'Includes gaming mouse'),
    ('MOD011', 'System 11', 'Brand K', 'Desktop', 2000.00, 1, '16GB', 'ASUS TUF B450M-PLUS GAMING', '29" LED', 'Intel Core i9', 'Includes gaming keyboard'),
    ('MOD012', 'System 12', 'Brand L', 'Laptop', 2800.00, 1, '12GB', 'MSI B450 GAMING PLUS', '14" LCD', 'AMD Ryzen 9', 'Includes external hard drive'),
    ('MOD013', 'System 13', 'Brand M', 'Desktop', 2100.00, 1, '8GB', 'ASUS ROG Strix B450-F', '25" LED', 'AMD Ryzen 7', 'Includes webcam cover'),
    ('MOD014', 'System 14', 'Brand N', 'Laptop', 2600.00, 1, '16GB', 'GIGABYTE B450M DS3H', '15.6" LCD', 'Intel Core i7', 'Includes laptop cooling pad'),
    ('MOD015', 'System 15', 'Brand O', 'Desktop', 2200.00, 1, '8GB', 'GIGABYTE B450 AORUS ELITE', '31" LED', 'AMD Ryzen 5', 'Includes USB hub');

-- Create Troubleshoot table
CREATE TABLE Troubleshoot (
    InvoiceNo NVARCHAR(38) PRIMARY KEY,
    CustomerName NVARCHAR(38),
    CustomerAddress NVARCHAR(38),
    CustomerPhoneNo NUMERIC(38),
    Problem NVARCHAR(38),
    ServiceDate DATE,
    Charge NUMERIC(38)
);
-- Inserting values in Troubleshoot table
INSERT INTO Troubleshoot (InvoiceNo, CustomerName, CustomerAddress, CustomerPhoneNo, Problem, ServiceDate, Charge)
VALUES
    ('INV001', 'Ali Khan', 'House No. 123, Lahore', 3123456789, 'Computer not booting', '2024-01-15', 500),
    ('INV002', 'Saba Ahmed', 'Flat No. 56, Karachi', 3339876543, 'Slow performance', '2024-01-18', 300),
    ('INV003', 'Ahmed Hassan', 'Street No. 10, Islamabad', 3012345678, 'Blue screen error', '2024-01-20', 700),
    ('INV004', 'Fatima Khan', 'House No. 789, Lahore', 3323456789, 'Virus infection', '2024-01-22', 450),
    ('INV005', 'Imran Malik', 'Apartment No. 34, Karachi', 3009876543, 'Data recovery', '2024-01-25', 600),
    ('INV006', 'Zainab Ali', 'Street No. 15, Islamabad', 3132345678, 'Hardware failure', '2024-01-28', 800),
    ('INV007', 'Naveed Ahmed', 'House No. 456, Lahore', 3333456789, 'Software installation', '2024-02-01', 350),
    ('INV008', 'Hina Khan', 'Flat No. 78, Karachi', 3149876543, 'Network connectivity issue', '2024-02-05', 550),
    ('INV009', 'Saad Ahmed', 'Street No. 20, Islamabad', 3022345678, 'Printer not working', '2024-02-10', 400),
    ('INV010', 'Aisha Malik', 'House No. 901, Lahore', 3336456789, 'Operating system upgrade', '2024-02-15', 750),
    ('INV011', 'Usman Ali', 'Apartment No. 12, Karachi', 3209876543, 'Data backup', '2024-02-20', 650),
    ('INV012', 'Sadia Ahmed', 'Street No. 30, Islamabad', 3152345678, 'System overheating', '2024-02-25', 900),
    ('INV013', 'Farhan Khan', 'House No. 345, Lahore', 3343456789, 'Keyboard replacement', '2024-03-01', 400),
    ('INV014', 'Saima Malik', 'Flat No. 89, Karachi', 3239876543, 'Mouse malfunction', '2024-03-05', 300),
    ('INV015', 'Bilal Ahmed', 'Street No. 40, Islamabad', 3162345678, 'Monitor flickering', '2024-03-10', 600);

-- Create Employee table
CREATE TABLE Employee (
    EmployeeID NVARCHAR(38) PRIMARY KEY,
    EmployeeName NVARCHAR(38),
    EmployeeAddress NVARCHAR(38),
    EmployeePhoneNo NUMERIC(38),
    EmailID NVARCHAR(38)
);
-- Inserting values in Employee table
INSERT INTO Employee (EmployeeID, EmployeeName, EmployeeAddress, EmployeePhoneNo, EmailID)
VALUES
    ('EMP001', 'Ali Raza', 'House No. 12, Lahore', 3212345678, 'ali.raza@example.com'),
    ('EMP002', 'Saba Khan', 'Flat No. 23, Karachi', 3329876543, 'saba.khan@example.com'),
    ('EMP003', 'Ahmed Ali', 'Street No. 45, Islamabad', 3034567890, 'ahmed.ali@example.com'),
    ('EMP004', 'Fatima Hassan', 'House No. 34, Lahore', 3432345678, 'fatima.hassan@example.com'),
    ('EMP005', 'Imran Khan', 'Apartment No. 56, Karachi', 3409876543, 'imran.khan@example.com'),
    ('EMP006', 'Zainab Raza', 'Street No. 67, Islamabad', 3134567890, 'zainab.raza@example.com'),
    ('EMP007', 'Naveed Ali', 'House No. 78, Lahore', 3532345678, 'naveed.ali@example.com'),
    ('EMP008', 'Hina Hassan', 'Flat No. 89, Karachi', 3349876543, 'hina.hassan@example.com'),
    ('EMP009', 'Saad Khan', 'Street No. 90, Islamabad', 3045678901, 'saad.khan@example.com'),
    ('EMP010', 'Aisha Ali', 'House No. 67, Lahore', 3632345678, 'aisha.ali@example.com'),
    ('EMP011', 'Usman Hassan', 'Apartment No. 78, Karachi', 3509876543, 'usman.hassan@example.com'),
    ('EMP012', 'Sadia Khan', 'Street No. 34, Islamabad', 3178901234, 'sadia.khan@example.com'),
    ('EMP013', 'Farhan Raza', 'House No. 23, Lahore', 3732345678, 'farhan.raza@example.com'),
    ('EMP014', 'Saima Ali', 'Flat No. 12, Karachi', 3639876543, 'saima.ali@example.com'),
    ('EMP015', 'Bilal Hassan', 'Street No. 56, Islamabad', 3189012345, 'bilal.hassan@example.com');

--Create table Warranty
CREATE TABLE Warranty (
    InvoiceNo NVARCHAR(38),
    SerialNo NVARCHAR(38) PRIMARY KEY,
    BillNo NVARCHAR(38),
    NewSerialNo NVARCHAR(38),
    Problem NVARCHAR(38),
    ServiceDate DATE,
    DeliveryDate DATE
);
--Inserting values in Warranty table 
INSERT INTO Warranty (InvoiceNo, SerialNo, BillNo, NewSerialNo, Problem, ServiceDate, DeliveryDate)
VALUES
    ('INV001', 'SN001', 'BN001', 'NewSN001', 'Screen flickering', '2023-01-15', '2023-01-20'),
    ('INV002', 'SN002', 'BN002', 'NewSN002', 'Keyboard malfunction', '2023-02-18', '2023-02-25'),
    ('INV003', 'SN003', 'BN003', 'NewSN003', 'Slow performance', '2023-03-20', '2023-03-28'),
    ('INV004', 'SN004', 'BN004', 'NewSN004', 'Hard disk failure', '2023-04-22', '2023-04-30'),
    ('INV005', 'SN005', 'BN005', 'NewSN005', 'System overheating', '2023-05-25', '2023-05-30'),
    ('INV006', 'SN006', 'BN006', 'NewSN006', 'Battery draining fast', '2023-06-28', '2023-07-05'),
    ('INV007', 'SN007', 'BN007', 'NewSN007', 'Operating system crash', '2023-07-01', '2023-07-08'),
    ('INV008', 'SN008', 'BN008', 'NewSN008', 'Printer not working', '2023-08-05', '2023-08-12'),
    ('INV009', 'SN009', 'BN009', 'NewSN009', 'Mouse not responsive', '2023-09-10', '2023-09-18'),
    ('INV010', 'SN010', 'BN010', 'NewSN010', 'Network connectivity issue', '2023-10-15', '2023-10-22'),
    ('INV011', 'SN011', 'BN011', 'NewSN011', 'Blue screen error', '2023-11-20', '2023-11-28'),
    ('INV012', 'SN012', 'BN012', 'NewSN012', 'Virus infection', '2023-12-25', '2023-12-30'),
    ('INV013', 'SN013', 'BN013', 'NewSN013', 'Software update failed', '2024-01-01', '2024-01-08'),
    ('INV014', 'SN014', 'BN014', 'NewSN014', 'Data recovery required', '2024-02-05', '2024-02-12'),
    ('INV015', 'SN015', 'BN015', 'NewSN015', 'System freezing', '2024-03-10', '2024-03-18');



--Add Customer Stored Procedure
CREATE PROCEDURE AddCustomer (
    @Customer_PhoneNo NUMERIC(38),
    @Customer_Name VARCHAR(38),
    @Customer_Address VARCHAR(38),
    @Customer_Balance NUMERIC(38)
)
AS
BEGIN
    INSERT INTO Customer (Customer_PhoneNo, Customer_Name, Customer_Address, Customer_Balance)
    VALUES (@Customer_PhoneNo, @Customer_name, @Customer_Address, @Customer_Balance);
END;


--Generate Sales Report Stored Procedure
CREATE PROCEDURE GenerateSalesReport (
    @StartDate DATE,
    @EndDate DATE
)
AS
BEGIN
    SELECT 
        InvoiceNo,
        Customer_Phone_no,
        Date,
        Totalamount,
        Paidamount,
        (Totalamount - Paidamount) AS Balance
    FROM Balance
    WHERE Date BETWEEN @StartDate AND @EndDate;
END;

--Troubleshooting Log Stored Procedure
CREATE PROCEDURE AddTroubleshootingLog (
    @InvoiceNo VARCHAR(5),
    @Customer_name VARCHAR(25),
    @Customer_Address VARCHAR(30),
    @Customer_Phone_no NUMERIC(10),
    @Problem VARCHAR(25),
    @Service_date DATE,
    @Charge NUMERIC(10)
)
AS
BEGIN
    INSERT INTO Troubleshoot (Invoice_no, Customer_name, Customer_Address, Customer_phoneno, Problem, Service_date, Charge)
    VALUES (@InvoiceNo, @Customer_name, @Customer_Address, @Customer_Phone_no, @Problem, @Service_date, @Charge);
END;

--Employee Search Stored Procedure
CREATE PROCEDURE SearchEmployee (
    @Employee_name VARCHAR(15)
)
AS
BEGIN
    SELECT *
    FROM Employee
    WHERE Employee_name LIKE '%' + @Employee_name + '%';
END;

--Crud operations
--1. Create(inserting or creating a new customer)
Insert Into Customer (CustomerID, CustomerName, CustomerAddress, CustomerPhoneNo, CustomerBalance)
Values ('16', 'Jhon Hubby', '123 Main str', '555-1234', '500.00');

--2. Read (selecting prev value)
select * from customer
where customerID =16;

--3. Update 
Update customer
set customername = 'Jane Jon', CustomerAddress='123 Avenue', CustomerBalance= 700
where customerID=16;

--4.Delete 
Delete from customer 
where customerID=16;


--Join
Select c.CustomerID, c.CustomerName, c.CustomerBalance, c.CustomerAddress , b.PaidAmount
From Customer c full outer join balance b
On c.customerID = b.CustomerID;