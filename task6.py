import random
import csv

class Worker:
    def __init__(self, name=None, surname=None, phoneNumber=None, salary=None, department=None):
        self.worker_id = random.randint(10000, 99999)
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Phone Number: {self.phoneNumber}, Salary: {self.salary}, Department: {self.department}"

    @property
    def worker_id(self):
        return self.__id
    
    @worker_id.setter
    def worker_id(self, value=None):
        self.__id = value

    @classmethod
    def read_workers_from_csv(cls, filename):
        workers = []
        try:
            with open(filename, newline="") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    worker = cls(
                        row.get('name', None),
                        row.get('surname', None),
                        row.get('phoneNumber', None),
                        row.get('salary', None),
                        row.get('department', None)
                    )
                    workers.append(worker)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return workers
    
    @classmethod
    def create_worker_from_user_input(cls):
        name = input("Name: ")
        surname = input("Surname: ")
        phoneNumber = input("Phone number: ")
        salary = input("Salary: ")
        department = input("Department: ")
        return cls(name, surname, phoneNumber, salary, department)
    
    @classmethod
    def search_workers(cls, filename, key, value):
        valid_workers = []
        try:
            with open(filename, newline="") as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    if row[key] == value:
                        worker = cls(
                            row.get('name', None),
                            row.get('surname', None),
                            row.get('phoneNumber', None),
                            row.get('salary', None),
                            row.get('department', None)
                        )
                        valid_workers.append(worker)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        return valid_workers
    
    @classmethod
    def add_worker_to_csv(cls, filename, worker):
        try:
            with open(filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([ worker.phoneNumber, worker.name, worker.surname, worker.salary, worker.department])
            print(f"Worker {worker.surname} added to the CSV file.")
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


if __name__ == "__main__":
    me = Worker.create_worker_from_user_input()
    print(me)
    print(me.worker_id)

    worker1 = Worker("Taras", "Shevchenko", "0566285193", 50000, "HR")
    Worker.add_worker_to_csv("text.csv", worker1)

    workers = Worker.read_workers_from_csv("text.csv")
    for i in workers:
        print(i)
        
    search_key = "department"
    search_value = "IT"
    found = Worker.search_workers("text.csv", search_key, search_value)
    for i in found:
        print(i)