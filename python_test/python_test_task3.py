class Employee:
    employees = []

    def __init__(self, name, employee_id, salary, role, extra_info):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.role = role
        self.extra_info = extra_info

        Employee.employees.append({
            "Name": self.name,
            "Employee ID": self.employee_id,
            "Salary": self.salary,
            "Role": self.role,
            "Extra Info": self.extra_info
        })

    @staticmethod
    def get_user_input():
        """It takes employee data from the user"""
        n = int(input("Enter the number of employees: "))

        for i in range(n):
            name = input("Name: ")
            employee_id = input("Employee ID: ")
            salary = int(input("Salary: "))
            role = input("Role (Manager/Developer): ")
            extra_info = input("Extra Info (Department for Manager or Programming Language for Developer): ")

            if role not in ["Manager", "Developer"]:
                print(f"Error: Invalid role '{role}'. Skipping this entry.")
                continue

            Employee(name, employee_id, salary, role, extra_info)

    @staticmethod
    def display_all_employees():
        """It displays the employee information"""
        if not Employee.employees:
            print("No employees to display.")
            return

        print("\nList of all employees:")
        for idx, emp in enumerate(Employee.employees):
            print(f"Employee {idx}:")
            for key, value in emp.items():
                print(f"  {key}: {value}")

    @staticmethod
    def filter_by_role(role):
        """It gives a list of employees based on their role"""
        role = role.capitalize()
        filtered = []

        for emp in Employee.employees:
            if emp["Role"] == role:
                filtered.append(emp)

        if not filtered:
            print(f"No employees found with role '{role}'.")
            return

        print(f"\nEmployees with role '{role}':")
        for emp in filtered:
            print(emp)

    @staticmethod
    def filter_by_salary(min_salary, max_salary):
        """It gives a list of employees based on their salary"""
        filtered = []

        for emp in Employee.employees:
            if min_salary <= emp["Salary"] <= max_salary:
                filtered.append(emp)

        if not filtered:
            print(f"No employees found with salary between {min_salary} and {max_salary}.")
            return

        print(f"\nEmployees with salary between {min_salary} and {max_salary}:")
        for emp in filtered:
            print(emp)

while True:
    print("1. Add Employee data \n2. Display all employees \n3. Filter employees by role. \n4. Filter employees by salary. \n5. Exit")
    choice = input(" Enter your choice:")
    match choice:
        case "1":
            Employee.get_user_input()
        case "2":
            Employee.display_all_employees()
        case "3":
            role_to_filter = input("\nEnter a role to filter employees (Manager/Developer): ")
            Employee.filter_by_role(role_to_filter)
        case "4":
            min_salary = int(input("\nEnter minimum salary to filter: "))
            max_salary = int(input("Enter maximum salary to filter: "))
            Employee.filter_by_salary(min_salary, max_salary)
        case "5":
            print("Existing..")
            break
        case _:
            print("Invalid option")

