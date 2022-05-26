from models.Employee import Employee
from models.Worker import Worker
from models.Foreman import Foreman
from models.Manager import Manager
from models.Scientist import Scientist


employee = Employee("Anton", 22, 9500)
print(employee)
employee.pay_salary()
print()

sales_manager = Manager("Anna", 40, 15000, 10)
print(sales_manager)
print()

inventor = Scientist("Andrew", 51, 20000, 8)
print(inventor)
print()

worker = Worker("Vasyl", 45, 13800, True)
print(worker)
print()

foreman = Foreman("Roman", 37, 17400, 9)
print(foreman)
