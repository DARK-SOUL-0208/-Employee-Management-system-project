# Employee Management System

## Overview
A modular Python console application for managing employee records.

## Features
- Add, view, search, update, and delete employees
- Validate employee information
- Generate employee statistics
- Persist records in `employees.json`

## Structure
```text
Employee Management System/
├── main.py
├── employees.json
└── modules/
    ├── employee.py
    ├── employee_manager.py
    ├── employee_update.py
    ├── employee_delete.py
    ├── reports.py
    └── validation.py
```

## Requirements
Python 3.x using the standard library.

## Run
```bash
python main.py
```

## Employee Report
The report calculates total employees, total salary, average salary, and employees by department.

## Storage
Records are stored in `employees.json`.

## Validation
The system checks basic employee details before storing records.

## Design
Separate modules handle employee operations, validation, reporting, and storage.

## Future Improvements
The system can later be extended with a GUI, database support, and authentication.

## Purpose
This project provides a simple way to manage employee information.
It is suitable for small-scale and academic use.

## Usage
Select an option from the menu and follow the prompts.
The program returns to the menu after completing an operation.
