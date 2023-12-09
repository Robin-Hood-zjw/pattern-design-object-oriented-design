from abc import ABC


class Employee(ABC):
    _id = None

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        sign = int(input('Please input an integer for gender: 0 for female, 1 for male, 2 for non-binary.\n'))
        while sign < 0 or sign > 2:
            sign = int(input('Please input an integer between 0 and 2.\n'))
        self.gender = sign

    def get_info(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        gender = 'female'
        if self.gender == 1:
            gender = 'male'
        elif self.gender == 2:
            gender == 'non-binary'
        print(f"Gender: {gender}")

    def get_employee_id(self) -> int:
        return -1 if self._id is None else self._id

    def add_employee_id(self, emp_id: int) -> None:
        if self._id is None:
          self._id = emp_id

    def __str__(self) -> str:
      gender = 'female'
      if self.gender == 1:
        gender = 'male'
      elif self.gender == 2:
        gender == 'non-binary'
      
      return f"Employee ID: {self._id}, Name: {self.name}, Age: {self.age}, Gender: {gender}"


class EmployeeSystem(ABC):
    def __init__(self) -> None:
        self.registered_employees = []

    def add_employee(self, employee: Employee) -> None:
      if employee.get_employee_id() == -1:
        last_id = self.registered_employees[-1].get_employee_id()
        employee.add_employee_id(last_id + 1)

      self.registered_employees.append(employee)


class Singleton(ABC):
    _instance = None

    def __init__(self) -> None:
        if self._instance is not None:
            raise Exception('The singleton instance has been initialized.')

        self._instance = EmployeeSystem()

    def input_employees_info(self) -> None:
        employee1 = Employee('James Bond', 35)
        employee2 = Employee('Albert Wayne', 50)
        employee3 = Employee('Erza Landon', 22)

        employee1.add_employee_id(1)
        employee2.add_employee_id(2)

        self._instance.add_employee(employee1)
        self._instance.add_employee(employee2)
        self._instance.add_employee(employee3)

    def print_singleton_info(self):
        for employee in self._instance.registered_employees:
            print(employee)


if __name__ == '__main__':
    instance = Singleton()
    instance.input_employees_info()
    instance.print_singleton_info()