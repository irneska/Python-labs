from models.Employee import Employee


class Scientist(Employee):
    def __init__(self, name: str, age: int, salary: float, number_of_inventions: int):
        super().__init__(name, age, salary)
        self._number_of_inventions = number_of_inventions

    def __str__(self):
        return f'In the age of {self._age} he has already created ' \
               f'{self._number_of_inventions} inventions'