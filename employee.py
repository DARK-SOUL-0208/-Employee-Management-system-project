class Employee:
    def __init__(self, employee_id, name, age, gender, department, designation, phone, email, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.designation = designation
        self.phone = phone
        self.email = email
        self.salary = salary

    def display(self):
        print("-" * 45)
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Age         :", self.age)
        print("Gender      :", self.gender)
        print("Department  :", self.department)
        print("Designation :", self.designation)
        print("Phone       :", self.phone)
        print("Email       :", self.email)
        print("Salary      :", self.salary)
        print("-" * 45)