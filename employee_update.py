from modules.employee_manager import load_employees, save_employees
from modules.validation import validate_name, validate_age, validate_gender, validate_text, validate_phone, validate_email, validate_salary
def update_employee():
    print("\n" + "=" * 45)
    print("UPDATE EMPLOYEE")
    print("=" * 45)
    employee_id = input("Enter Employee ID to update: ").strip()
    employees = load_employees()
    employee = None
    for data in employees:
        if data["employee_id"] == employee_id:
            employee = data
            break
    if employee is None:
        print("\nEmployee not found.")
        return
    print("\nEmployee found.")
    print("Enter the new details.")
    while True:
        name = input("Enter New Name: ").strip()
        if validate_name(name):
            break
        print("Invalid name. Please use letters and spaces only.")
    while True:
        age = input("Enter New Age: ").strip()
        if validate_age(age):
            age = int(age)
            break
        print("Invalid age. Enter a number between 18 and 70.")
    while True:
        gender = input("Enter New Gender: ").strip()
        if validate_gender(gender):
            gender = gender.capitalize()
            break
        print("Invalid gender. Enter Male, Female, or Other.")
    while True:
        department = input("Enter New Department: ").strip()
        if validate_text(department):
            break
        print("Invalid department.")
    while True:
        designation = input("Enter New Designation: ").strip()
        if validate_text(designation):
            break
        print("Invalid designation.")
    while True:
        phone = input("Enter New Phone Number: ").strip()
        if validate_phone(phone):
            break
        print("Invalid phone number. Enter exactly 10 digits.")
    while True:
        email = input("Enter New Email: ").strip()
        if validate_email(email):
            break
        print("Invalid email address.")
    while True:
        salary = input("Enter New Salary: ").strip()
        if validate_salary(salary):
            salary = float(salary)
            break
        print("Invalid salary.")
    print("\n" + "=" * 45)
    print("NEW DETAILS")
    print("=" * 45)
    print("Employee ID:", employee_id)
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Department:", department)
    print("Designation:", designation)
    print("Phone:", phone)
    print("Email:", email)
    print("Salary:", salary)
    print("=" * 45)
    confirm = input("\nSave these changes? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("\nUpdate cancelled.")
        return
    employee["name"] = name
    employee["age"] = age
    employee["gender"] = gender
    employee["department"] = department
    employee["designation"] = designation
    employee["phone"] = phone
    employee["email"] = email
    employee["salary"] = salary
    save_employees(employees)
    print("\nEmployee updated successfully!")
