import json
import os
from modules.employee import Employee
from modules.validation import validate_name, validate_age, validate_gender, validate_text, validate_phone, validate_email, validate_salary

FILE_NAME = "employees.json"
def load_employees():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)
def add_employee():
    print("\n" + "=" * 45)
    print("ADD EMPLOYEE")
    print("=" * 45)
    employees = load_employees()
    while True:
        employee_id = input("Enter Employee ID: ").strip()
        if employee_id == "":
            print("Employee ID cannot be empty.")
            continue
        found = False
        for employee in employees:
            if employee["employee_id"] == employee_id:
                found = True
                break
        if found:
            print("Employee ID already exists. Please enter a different ID.")
        else:
            break
    while True:
        name = input("Enter Employee Name: ").strip()
        if validate_name(name):
            break
        print("Invalid name. Please use letters and spaces only.")
    while True:
        age = input("Enter Age: ").strip()
        if validate_age(age):
            age = int(age)
            break
        print("Invalid age. Enter a number between 18 and 70.")
    while True:
        gender = input("Enter Gender: ").strip()
        if validate_gender(gender):
            gender = gender.capitalize()
            break
        print("Invalid gender. Enter Male, Female, or Other.")
    while True:
        department = input("Enter Department: ").strip()
        if validate_text(department):
            break
        print("Invalid department.")
    while True:
        designation = input("Enter Designation: ").strip()
        if validate_text(designation):
            break
        print("Invalid designation.")
    while True:
        phone = input("Enter Phone Number: ").strip()
        if validate_phone(phone):
            break
        print("Invalid phone number. Enter exactly 10 digits.")
    while True:
        email = input("Enter Email: ").strip()
        if validate_email(email):
            break
        print("Invalid email address.")
    while True:
        salary = input("Enter Salary: ").strip()
        if validate_salary(salary):
            salary = float(salary)
            break
        print("Invalid salary. Enter a valid number.")
    employee = Employee(employee_id, name, age, gender, department, designation, phone, email, salary)
    employee_data = {"employee_id": employee.employee_id, "name": employee.name, "age": employee.age, "gender": employee.gender, "department": employee.department, "designation": employee.designation, "phone": employee.phone, "email": employee.email, "salary": employee.salary}
    employees.append(employee_data)
    save_employees(employees)
    print("\nEmployee added successfully!")
def view_employees():
    employees = load_employees()
    if not employees:
        print("\nNo employees found.")
        return
    print("\n" + "=" * 80)
    print("EMPLOYEE LIST")
    print("=" * 80)
    for data in employees:
        employee = Employee(data["employee_id"], data["name"], data["age"], data["gender"], data["department"], data["designation"], data["phone"], data["email"], data["salary"])
        employee.display()
def search_employee():
    print("\n" + "=" * 45)
    print("SEARCH EMPLOYEE")
    print("=" * 45)
    employee_id = input("Enter Employee ID to search: ").strip()
    employees = load_employees()
    for data in employees:
        if data["employee_id"] == employee_id:
            employee = Employee(data["employee_id"], data["name"], data["age"], data["gender"], data["department"], data["designation"], data["phone"], data["email"], data["salary"])
            print("\nEmployee Found:")
            employee.display()
            return
    print("\nEmployee not found.")
