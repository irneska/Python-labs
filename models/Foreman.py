from models.Employee import Employee


class Foreman(Employee):
    def __init__(self, name: str, age: int, salary: float, number_of_subordinates: int):
        super().__init__(name, age, salary)
        self._number_of_subordinates = number_of_subordinates

    def __str__(self):
        return f'If the foreman has more than {self._number_of_subordinates} subordinates, ' \
               f'work will be done till the next week'