class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self._name = name
        self._age = age
        self._salary = salary

    def __str__(self):
        return f'Employee {self._name} age {self._age} get salary {self._salary}'

    def pay_salary(self):
        print(f'Salary ${self._salary} is paid to {self._name} ')