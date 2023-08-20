
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f'Name: {self.name} -- Salary: {self.salary}')\
        
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print(f"Bonus: {self.bonus}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def display_info(self):
        super().display_info()
        print(f"Programming language: {self.programming_language}")



employee = Employee('Kien', 3000)
employee.display_info()
print("-----------")
manager = Manager('Trung', 2000, 1000)
manager.display_info()
print("-----------")
developer = Developer('Duong', 5000, 2000)
developer.display_info()
