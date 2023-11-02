from worker import *
from database import WorkerDatabase

if __name__ == "__main__":
    a = WorkerDatabase("text.csv")
    print(a)
    a.sort_by_param("name")
    print(a)
    g = a.create_worker_from_user_input()
    de = a.create_worker_from_user_input(Delivery)
    no = a.create_worker_from_user_input(Non_Delivery)
    idishka = input("Enter ID to delete: ")
    a.delete_worker(int(idishka))
    edit_idishka = input("Enter ID to edit: ")
    a.edit_worker(int(edit_idishka), 'name', 'Anon')