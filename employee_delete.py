from modules.employee_manager import load_employees, save_employees

def delete_employee():
    print("\n" + "=" * 45)
    print("DELETE EMPLOYEE")
    print("=" * 45)
    employee_id = input("Enter Employee ID to delete: ").strip()
    employees = load_employees()
    employee = None
    for data in employees:
        if data["employee_id"] == employee_id:
            employee = data
            break
    if employee is None:
        print("\nEmployee not found.")
        return
    print("\nEmployee found:")
    print("-" * 40)
    print("Employee ID:", employee["employee_id"])
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Designation:", employee["designation"])
    print("-" * 40)
    confirm = input("\nAre you sure you want to delete this employee? (yes/no): ").strip().lower()
    if confirm == "yes":
        employees.remove(employee)
        save_employees(employees)
        print("\nEmployee deleted successfully!")
    else:
        print("\nDelete cancelled.")