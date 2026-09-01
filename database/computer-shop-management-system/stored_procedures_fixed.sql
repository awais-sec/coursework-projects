-- ============================================================
-- Fixed stored procedures for Computer Shop Management System
-- Corrected to match the actual table definitions in
-- Project Queries of computer shop managment system(008).sql
-- ============================================================

-- Add Customer Stored Procedure
-- Fix: original referenced Customer_PhoneNo/Customer_Name/Customer_Address/
-- Customer_Balance, which don't exist. Real columns are CustomerID,
-- CustomerName, CustomerAddress, CustomerPhoneNo, CustomerBalance.
-- CustomerID is the primary key with no identity/default, so it must
-- be supplied as a parameter.
CREATE PROCEDURE AddCustomer (
    @CustomerID INT,
    @CustomerName NVARCHAR(50),
    @CustomerAddress NVARCHAR(100),
    @CustomerPhoneNo NVARCHAR(15),
    @CustomerBalance DECIMAL(15, 2)
)
AS
BEGIN
    INSERT INTO Customer (CustomerID, CustomerName, CustomerAddress, CustomerPhoneNo, CustomerBalance)
    VALUES (@CustomerID, @CustomerName, @CustomerAddress, @CustomerPhoneNo, @CustomerBalance);
END;
GO

-- Generate Sales Report Stored Procedure
-- Fix: original selected Customer_Phone_no, Totalamount, Paidamount, Date
-- from Balance, but Balance has no phone number column and its actual
-- columns are PaidAmount, TotalAmount, Dat (not Date). Phone number now
-- comes from a join to Customer.
CREATE PROCEDURE GenerateSalesReport (
    @StartDate DATE,
    @EndDate DATE
)
AS
BEGIN
    SELECT
        b.InvoiceNo,
        c.CustomerPhoneNo,
        b.Dat AS SaleDate,
        b.TotalAmount,
        b.PaidAmount,
        (b.TotalAmount - b.PaidAmount) AS Balance
    FROM Balance b
    JOIN Customer c ON b.CustomerID = c.CustomerID
    WHERE b.Dat BETWEEN @StartDate AND @EndDate;
END;
GO

-- Troubleshooting Log Stored Procedure
-- Fix: original referenced Invoice_no/Customer_name/Customer_Address/
-- Customer_phoneno/Service_date, which don't match the actual
-- Troubleshoot table columns (InvoiceNo, CustomerName, CustomerAddress,
-- CustomerPhoneNo, Problem, ServiceDate, Charge).
CREATE PROCEDURE AddTroubleshootingLog (
    @InvoiceNo NVARCHAR(38),
    @CustomerName NVARCHAR(38),
    @CustomerAddress NVARCHAR(38),
    @CustomerPhoneNo NUMERIC(38),
    @Problem NVARCHAR(38),
    @ServiceDate DATE,
    @Charge NUMERIC(38)
)
AS
BEGIN
    INSERT INTO Troubleshoot (InvoiceNo, CustomerName, CustomerAddress, CustomerPhoneNo, Problem, ServiceDate, Charge)
    VALUES (@InvoiceNo, @CustomerName, @CustomerAddress, @CustomerPhoneNo, @Problem, @ServiceDate, @Charge);
END;
GO

-- Employee Search Stored Procedure
-- No fix needed: EmployeeName parameter and table column already match.
CREATE PROCEDURE SearchEmployee (
    @EmployeeName NVARCHAR(38)
)
AS
BEGIN
    SELECT *
    FROM Employee
    WHERE EmployeeName LIKE '%' + @EmployeeName + '%';
END;
GO
