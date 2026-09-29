from modules.employee_manager import add_employee, view_employees, search_employee
from modules.employee_update import update_employee
from modules.employee_delete import delete_employee
from modules.reports import employee_report
def employee_management():
    while True:
        print("\n" + "=" * 50)
        print("EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Employee Report")
        print("7. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            employee_report()
        elif choice == "7":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please enter 1 to 7.")
if __name__ == "__main__":
    employee_management()
