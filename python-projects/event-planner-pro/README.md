# Event Planner Pro

A desktop event-booking manager built with Tkinter and SQLite. This coursework project covers user registration/login, booking management, calendar-based viewing, and basic booking statistics.

## Features

- User registration and login
- Password storage using salted PBKDF2-HMAC-SHA256
- Add, view, and delete event bookings
- Booking fields for customer, date, event type, services, menu, headcount, and estimated cost
- Calendar view for scheduled bookings
- Statistics for total bookings, monthly bookings, and estimated revenue
- SQLite database created automatically on first run

## Requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
python event_planner.py
```

## Workflow

```text
Register / Login
       ↓
   Dashboard
   ├── Add Booking
   ├── View / Delete Bookings
   ├── Calendar View
   └── Statistics
       ↓
    SQLite Database
```

## Technical Focus

- Python GUI development with Tkinter
- SQLite database operations
- Parameterized SQL queries
- Password hashing with PBKDF2-HMAC-SHA256
- Form validation and basic application state handling

## Scope

This is an academic desktop application demonstrating Python, GUI, database, and authentication concepts. It is not intended as a production booking system.
