import random

class Worker:
    def __init__(self, name=None, surname=None, phoneNumber=None, salary=None, department=None):
        self.__id = random.randint(10000, 99999)
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"ID: {self.worker_id} ,Name: {self.name}, Surname: {self.surname}, Phone Number: {self.phoneNumber}, Salary: {self.salary}, Department: {self.department}"

    @property
    def worker_id(self):
        return self.__id
    
    @worker_id.setter
    def worker_id(self, value=None):
        self.__id = value

class Delivery(Worker):
    def __init__(self, name, surname, phoneNumber, salary, department, duty):
        super().__init__(name, surname, phoneNumber, salary, department)
        self.duty = duty

    def __str__(self):
        info = super().__str__()
        return f"{info}, Duty: {self.duty}"
    
class Non_Delivery(Worker):
    def __init__(self, name, surname, phoneNumber, salary, department, jobTitle):
        super().__init__(name, surname, phoneNumber, salary, department)
        self.jobTitle = jobTitle

    def __str__(self):
        info = super().__str__()
        return f"{info}, Job Title : {self.jobTitle}"