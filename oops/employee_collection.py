class Employee:

    def __init__(self, emp_id, name, department, company, salary, certified):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.company = company
        self.salary = salary
        self.certified = certified

    def __str__(self):
        return (f"Employee ID : {self.emp_id}\n"
                f"Name        : {self.name}\n"
                f"Department  : {self.department}\n"
                f"Company     : {self.company}\n"
                f"Salary      : {self.salary}\n"
                f"Certified   : {self.certified}")


class EmployeeManagement:

    def __init__(self):
        self.employee_list = []

    # 1. Add Employee
    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employee_list.append(employee)
            return True
        return False

    # 2. Return Employee Dictionary
    def get_employee_dictionary(self):
        emp_dict = {}

        for emp in self.employee_list:
            emp_dict[emp.emp_id] = {
                "Name": emp.name,
                "Department": emp.department,
                "Company": emp.company,
                "Salary": emp.salary,
                "Certified": emp.certified
            }

        return emp_dict

    # 3. Total Employees Company Wise
    def total_employee_company(self, company):
        count = 0

        for emp in self.employee_list:
            if emp.company.lower() == company.lower():
                count += 1

        return count

    # Total Employees Department Wise
    def total_employee_department(self, department):
        count = 0

        for emp in self.employee_list:
            if emp.department.lower() == department.lower():
                count += 1

        return count

    # 4. Available Departments
    def get_departments(self):

        dept = set()

        for emp in self.employee_list:
            dept.add(emp.department)

        return list(dept)

    # 5. Average Salary Department Wise
    def average_salary_department(self, department):

        salary = []

        for emp in self.employee_list:
            if emp.department.lower() == department.lower():
                salary.append(emp.salary)

        if len(salary) == 0:
            return 0

        return sum(salary) / len(salary)

    # Average Salary Company Wise
    def average_salary_company(self, company):

        salary = []

        for emp in self.employee_list:
            if emp.company.lower() == company.lower():
                salary.append(emp.salary)

        if len(salary) == 0:
            return 0

        return sum(salary) / len(salary)

    # 6. Certified Employees Department Wise
    def certified_department(self, department):

        count = 0

        for emp in self.employee_list:
            if emp.department.lower() == department.lower() and emp.certified:
                count += 1

        return count

    # Certified Employees Company Wise
    def certified_company(self, company):

        count = 0

        for emp in self.employee_list:
            if emp.company.lower() == company.lower() and emp.certified:
                count += 1

        return count

    # 7. Department Status
    def department_status(self):

        status = {}

        for emp in self.employee_list:

            if emp.department in status:
                status[emp.department] += 1
            else:
                status[emp.department] = 1

        return status

    # 8. Highest Paid Employee Department Wise
    def highest_paid_department(self, department):

        employees = []

        for emp in self.employee_list:
            if emp.department.lower() == department.lower():
                employees.append(emp)

        if len(employees) == 0:
            return None

        return max(employees, key=lambda x: x.salary)

    # Highest Paid Employee Company Wise
    def highest_paid_company(self, company):

        employees = []

        for emp in self.employee_list:
            if emp.company.lower() == company.lower():
                employees.append(emp)

        if len(employees) == 0:
            return None

        return max(employees, key=lambda x: x.salary)


if __name__ == "__main__":

    manager = EmployeeManagement()

    e1 = Employee(101, "Ankit", "IT", "TCS", 50000, True)
    e2 = Employee(102, "Rahul", "HR", "TCS", 45000, False)
    e3 = Employee(103, "Priya", "IT", "Infosys", 70000, True)
    e4 = Employee(104, "Neha", "Finance", "TCS", 65000, True)
    e5 = Employee(105, "Amit", "IT", "TCS", 80000, False)
    e6 = Employee(106, "Riya", "HR", "Infosys", 60000, True)

    manager.add_employee(e1)
    manager.add_employee(e2)
    manager.add_employee(e3)
    manager.add_employee(e4)
    manager.add_employee(e5)
    manager.add_employee(e6)

    print("\nEmployee Dictionary")
    print(manager.get_employee_dictionary())

    print("\nTotal Employees Company Wise")
    print("TCS :", manager.total_employee_company("TCS"))
    print("Infosys :", manager.total_employee_company("Infosys"))

    print("\nTotal Employees Department Wise")
    print("IT :", manager.total_employee_department("IT"))
    print("HR :", manager.total_employee_department("HR"))

    print("\nAvailable Departments")
    print(manager.get_departments())

    print("\nAverage Salary")
    print("IT :", manager.average_salary_department("IT"))
    print("TCS :", manager.average_salary_company("TCS"))

    print("\nCertified Employees")
    print("IT :", manager.certified_department("IT"))
    print("TCS :", manager.certified_company("TCS"))

    print("\nDepartment Status")
    print(manager.department_status())

    print("\nHighest Paid Employee (Department Wise)")
    emp = manager.highest_paid_department("IT")
    if emp:
        print(emp)

    print("\nHighest Paid Employee (Company Wise)")
    emp = manager.highest_paid_company("TCS")
    if emp:
        print(emp)
