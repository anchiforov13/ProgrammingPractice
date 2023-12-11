from worker import *
from database import WorkerDatabase
import pandas as pd
import matplotlib.pyplot as plt
from worker_tkinter import WorkerApp
import tkinter as tk

if __name__ == "__main__":
    db = WorkerDatabase("text.csv")
    # db.plot_future_salary_increase(1, 24)
    # db.plot_future_salary_increase(4, 24)
    # db.plot_future_salary_increase(5, 24)
    # dataframe = pd.read_csv('text.csv')
    # departments = dataframe['department'].value_counts()
    # departments.plot.pie(autopct='%1.1f%%', startangle=90)
    # plt.show()
    root = tk.Tk()
    app = WorkerApp(root, db)
    root.mainloop()