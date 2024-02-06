from abc import ABC

class Person(ABC):
    def get_name(self):
        pass

class Employee(Person):
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

class Manager(Person):
    def __init__(self, name) -> None:
        self.name = name
    
    def get_name(self) -> str:
        return self.name

class Team(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.manager = None
        self.employees = list()

    def get_team_name(self) -> str:
        return self.name

    def assign_manager(self, manager: Manager) -> None:
        self.manager = manager

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def delete_employee(self, employee: Employee) -> None:
        for uniq_employee in self.employees.copy():
            if uniq_employee.get_name() == employee.get_name():
                self.employees.remove(uniq_employee)

    def print_team_info(self) -> None:
        if self.manager:
            print(f'Manager: {self.manager.get_name()}')
            
        for employee in self.employees:
            print(f'Employee: {employee.get_name()}')
        print('\n')

class Department(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.teams = dict()
    
    def get_name(self) -> str:
        return self.name

    def add_employee(self, team_name: str, employee: Employee) -> None:
        self.teams[team_name].add_employee(employee)

    def create_team(self, name: str, manager: str) -> None:
        team = Team(name)
        team.assign_manager(Manager(manager))
        self.teams[name] = team

    def delete_team(self, name: str) -> None:
        if name in self.teams:
            del self.teams[name]

    def print_department_info(self):
        print(f'Department: {self.get_name()}\n')
        for val in self.teams.values():
            print(f'Team: {val.get_team_name()}')
            val.print_team_info()

class Company(ABC):
    def __init__(self, name: str, year: int) -> None:
        self.name = name
        self.year = year
        self.departments = dict()

    def add_department(self, department: Department) -> None:
        self.departments[department.get_name()] = department

    def print_company_info(self) -> None:
        print(f'{self.name} founded in {self.year}.')

    def print_department_info(self, name: str) -> None:
        for department in self.departments.values():
            if department.get_name() == name:
                self.print_company_info()
                department.print_department_info()

if __name__ == '__main__':
    manager = Manager('Gambit')
    employee1 = Employee('Erza Landon')
    employee2 = Employee('Charles Xavier')
    employee3 = Employee('Erik Lehnsherr')

    department1 = Department('Department 1')
    department1.create_team('Team X', 'Gambit')
    department1.add_employee('Team X', employee1)
    department1.add_employee('Team X', employee2)
    department1.add_employee('Team X', employee1)

    company1 = Company('Apple, Inc.', 1976)
    company1.add_department(department1)

    company1.print_department_info('Department 1')
