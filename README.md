# Student Management System

A console application to manage student records. It supports adding, viewing, searching, updating and deleting students, with input validation.

## Features
- Add, view, search, update and delete students (CRUD)
- Validation for name, email and marks (0 to 100)
- Duplicate email protection
- Data saved permanently in a SQLite database

## Tech Used
- Python 3
- SQLite (`sqlite3` module, built into Python)

## How to Run
```
python main.py
```
The database file `student.db` is created automatically on the first run.

## Project Structure
- `main.py`: menu and user input
- `db.py`: all database functions

## Table Structure: STUDENT_TABLE

| Column | Type | Rules |
|---|---|---|
| ID | INTEGER | Primary key, auto-increment |
| NAME | VARCHAR(20) | Required |
| EMAIL | VARCHAR(100) | Unique |
| COURSE | VARCHAR(30) | |
| MARK | REAL | Between 0 and 100 |


