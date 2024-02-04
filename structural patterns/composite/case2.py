from abc import ABC, abstractmethod


class Unit(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Employee(Unit):
    def __init__(self, name) -> None:
        self.name = name

    def print_info(self) -> None:
        print(f'    {self.name}')

class Department(Unit):
    def __init__(self, name) -> None:
        self.name = name
        self.employees = list()

    def print_info(self) -> None:
        print(f'  {self.name}')

        for employee in self.employees:
            employee.print_info()

    def add_employee(self, employee) -> None:
        self.employees.append(employee)

class Company(Unit):
    def __init__(self, name) -> None:
        self.name = name
        self.departments = list()

    def print_info(self) -> None:
        print(self.name)

        for department in self.departments:
            department.print_info()

    def add_department(self, department) -> None:
        self.departments.append(department)



if __name__ == '__main__':
    company = Company('Autodesk, Inc.')

    department_A = Department('Department A')
    department_B = Department('Department B')
    department_C = Department('Department C')

    department_A.add_employee(Employee('Andrew'))
    department_A.add_employee(Employee('Buck'))
    department_A.add_employee(Employee('Charlie'))

    department_B.add_employee(Employee('Dallas'))
    department_B.add_employee(Employee('Elsa'))
    department_B.add_employee(Employee('Fiona'))

    department_C.add_employee(Employee('Glabia'))
    department_C.add_employee(Employee('Helen'))
    department_C.add_employee(Employee('Ivan'))

    company.add_department(department_A)
    company.add_department(department_B)
    company.add_department(department_C)

    company.print_info()