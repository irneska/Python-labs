from models import Employee, Worker, Foreman, Manager, Scientist


employee = Employee.Employee("Anton", 22, 9500)
print(str(employee))
employee.pay_salary()
print()

sales_manager = Manager.Manager("Anna", 40, 15000, 10)
print(str(sales_manager))
print()

inventor = Scientist.Scientist("Andrew", 51, 20000, 8)
print(str(inventor))
print()

worker = Worker.Worker("Vasyl", 45, 13800, True)
print(str(worker))
print()

foreman = Foreman.Foreman("Roman", 37, 17400, 9)
print(str(foreman))
