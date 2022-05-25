from models.Employee import Employee


class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float, work_experience: float):
        super().__init__(name, age, salary)
        self.work_experience = work_experience

    def __str__(self):
        return f'The manager {self._name} has been working in our ' \
               f'company for {self.work_experience} years'
