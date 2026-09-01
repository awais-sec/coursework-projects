# Computer Shop Management System

A relational database project for managing a computer retail/service shop: customers, inventory (parts and systems), sales, employees, warranties, and repair tickets.

## Schema

7 tables: `Customer`, `Balance`, `ComputerPartDetail`, `ComputerSystemDetail`, `Troubleshoot`, `Employee`, `Warranty`.

`schema.sql` contains the full table definitions, sample data (15 rows per table), CRUD examples, and a join between `Customer` and `Balance`.

`stored_procedures_fixed.sql` contains four stored procedures (add customer, generate sales report, log a troubleshooting ticket, search employees), corrected to match the final table structure — see note below.

## Diagrams

`erd.png` and `schema-diagram.png` are early design iterations from before the schema was finalized, kept here to show the design process. They don't fully match the final 7-table schema in `schema.sql` — the final schema is the source of truth.

## Note on the stored procedures

The stored procedures were originally written against an earlier, slightly different version of the column names (e.g. `Customer_Name` instead of `CustomerName`) and would not execute against the final schema. `stored_procedures_fixed.sql` corrects the parameter and column names to match the tables in `schema.sql`.
