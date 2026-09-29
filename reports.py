from modules.employee_manager import load_employees
def employee_report():
    employees = load_employees()
    total_employees = len(employees)
    total_salary = 0
    for employee in employees:
        total_salary += employee["salary"]
    if total_employees == 0:
        average_salary = 0
    else:
        average_salary = total_salary / total_employees
    departments = {}
    for employee in employees:
        department = employee["department"]
        if department not in departments:
            departments[department] = 1
        else:
            departments[department] += 1
    print("\n" + "=" * 50)
    print("EMPLOYEE REPORT")
    print("=" * 50)
    print("\nTotal Employees:", total_employees)
    print("Total Salary:", format(total_salary, ".2f"))
    print("Average Salary:", format(average_salary, ".2f"))
    print("\nEmployees by Department:")
    print("-" * 30)
    if len(departments) == 0:
        print("No department data available.")
    else:
        for department in departments:
            print(department + ":", departments[department])
    print("=" * 50)
