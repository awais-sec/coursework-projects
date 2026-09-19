# Event Planner Pro

A desktop event-booking manager built with Tkinter and SQLite. I built this to
manage bookings for events end to end: register/login, add and review
bookings, browse them on a calendar, and see quick stats.

## Features

- User registration and login (passwords hashed with salted PBKDF2-HMAC)
- Add, view, and delete event bookings (customer, date, type, services, menu, headcount, cost)
- Calendar view showing which dates have bookings
- Stats screen (total bookings, bookings this month, total estimated revenue)

## Requirements

```
pip install -r requirements.txt
```

## Run

```
python event_planner.py
```

The SQLite database (`event_planner.db`) is created automatically on first run.
