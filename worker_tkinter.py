import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
from worker import *

class WorkerApp:
    def __init__(self, root, worker_database):
        self.root = root
        self.root.title("Worker Database App")
        self.worker_database = worker_database

        self.root.geometry("400x400")
        style = ttk.Style()
        style.configure("TButton", padding=(10, 5), font=('Helvetica', 12))

        self.add_button = ttk.Button(self.root, text="Add Worker", command=self.add_worker)
        self.add_button.pack(pady=10)

        self.edit_button = ttk.Button(self.root, text="Edit Worker", command=self.edit_worker)
        self.edit_button.pack(pady=10)

        self.delete_button = ttk.Button(self.root, text="Delete Worker", command=self.delete_worker)
        self.delete_button.pack(pady=10)

        self.search_button = ttk.Button(self.root, text="Search Workers", command=self.search_workers)
        self.search_button.pack(pady=10)

        self.sort_button = ttk.Button(self.root, text="Sort Workers", command=self.sort_workers)
        self.sort_button.pack(pady=10)

    def add_worker(self):
        name = simpledialog.askstring("Input", "Name:")
        surname = simpledialog.askstring("Input", "Surname:")
        phoneNumber = simpledialog.askstring("Input", "Phone Number:")
        salary = simpledialog.askinteger("Input", "Salary:")
        department = simpledialog.askstring("Input", "Department:")
        subclass = simpledialog.askstring("Input", "Delivery or Non-Delivery? (1 or 2)")
        if subclass == "1":
            duty = simpledialog.askstring("Input", "Duty:")
            new_worker = Delivery(name, surname, phoneNumber, salary, department, duty)
        elif subclass == "2":
            jobTitle = simpledialog.askstring("Input", "Job Title:")
            new_worker = Non_Delivery(name, surname, phoneNumber, salary, department, jobTitle)
        else:
            new_worker = Worker(name, surname, phoneNumber, salary, department)
        self.worker_database.add_worker_to_csv(new_worker)
        messagebox.showinfo("Success", f"Worker {new_worker.surname} added successfully.")
        return new_worker

    def edit_worker(self):
        worker_id = simpledialog.askinteger("Input", "Enter Worker ID:")
        if worker_id:
            param = simpledialog.askstring("Input", "Enter Parameter to Edit:")
            value = simpledialog.askstring("Input", "Enter New Value:")
            self.worker_database.edit_worker(worker_id, param, value)
            messagebox.showinfo("Success", f"Worker with ID {worker_id} edited successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a valid Worker ID.")

    def delete_worker(self):
        worker_id = simpledialog.askinteger("Input", "Enter Worker ID:")
        if worker_id:
            self.worker_database.delete_worker(worker_id)
            messagebox.showinfo("Success", f"Worker with ID {worker_id} deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a valid Worker ID.")

    def search_workers(self):
        key = simpledialog.askstring("Input", "Enter Search Key:")
        value = simpledialog.askstring("Input", "Enter Search Value:")
        search_results = self.worker_database.search_workers(key, value)
        if search_results:
            messagebox.showinfo("Search Results", "\n".join(str(worker) for worker in search_results))
        else:
            messagebox.showinfo("Search Results", "No matching workers found.")

    def sort_workers(self):
        param = simpledialog.askstring("Input", "Enter Parameter to Sort By:")
        sorted_workers = self.worker_database.sort_by_param(param)
        if sorted_workers:
            messagebox.showinfo("Sorted Workers", "\n".join(str(worker) for worker in sorted_workers))
        else:
            messagebox.showwarning("Warning", "Invalid sorting parameter or no workers to sort.")