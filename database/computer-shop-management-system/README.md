# Computer Shop Management System

A relational database coursework project for managing a computer retail and service shop, covering customers, balances, computer parts, systems, troubleshooting records, employees, and warranties.

## Database Structure

The final schema contains seven tables:

- `Customer`
- `Balance`
- `ComputerPartDetail`
- `ComputerSystemDetail`
- `Troubleshoot`
- `Employee`
- `Warranty`

`schema.sql` contains the table definitions, sample data, CRUD examples, and a customer/balance join.

## Stored Procedures

`stored_procedures_fixed.sql` contains four corrected procedures:

- `AddCustomer`
- `GenerateSalesReport`
- `AddTroubleshootingLog`
- `SearchEmployee`

The separate fixed file is intentional: the original coursework procedures referenced older column names that no longer matched the final schema. The corrected version aligns the procedure parameters and queries with the current tables.

## Design Artifacts

- `erd.png`
- `schema-diagram.png`

These diagrams are retained as earlier design iterations. They do not fully match the final seven-table schema; `schema.sql` is the source of truth.

## Workflow

```text
Requirements / Shop Functions
          ↓
      Table Design
          ↓
      Sample Data
          ↓
   CRUD + Relational Queries
          ↓
    Stored Procedures
          ↓
   Schema / Design Review
```

## Technical Focus

- Microsoft SQL Server / T-SQL
- Relational schema design
- Primary and foreign keys
- CRUD operations
- Joins
- Stored procedures
- Sample data modeling
- Database design documentation

## Scope

This is an academic database project preserved as coursework evidence. It is not intended to represent a production-ready retail or service database.
