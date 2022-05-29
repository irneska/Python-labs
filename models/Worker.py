from models.Employee import Employee


class Worker(Employee):
    def __init__(self, name: str, age: int, salary: float, has_assistant: bool):
        super().__init__(name, age, salary)
        self._has_assistant = has_assistant

    def __str__(self):
        return f'The average salary of our workers is ${self._salary}'