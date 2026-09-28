from modules.employee_manager import load_employees

def employee_report():
    employees = load_employees()
    total_employees = len(employees)
    total_salary = 0
    for employee in employees:
        total_salary += employee["salary"]
    if total_employees > 0:
        average_salary = total_salary / total_employees
    else:
        average_salary = 0
    departments = {}
    for employee in employees:
        department = employee["department"]
        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1
    print("\n" + "=" * 50)
    print("EMPLOYEE REPORT")
    print("=" * 50)
    print(f"\nTotal Employees: {total_employees}")
    print(f"Total Salary: {total_salary:.2f}")
    print(f"Average Salary: {average_salary:.2f}")
    print("\nEmployees by Department:")
    print("-" * 30)
    if departments:
        for department, count in departments.items():
            print(f"{department}: {count}")
    else:
        print("No department data available.")
    print("=" * 50)
