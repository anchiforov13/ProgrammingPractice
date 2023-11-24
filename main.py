from worker import *
from database import WorkerDatabase

if __name__ == "__main__":
    db = WorkerDatabase("text.csv")
    db.plot_future_salary_increase(1, 24)
    db.plot_future_salary_increase(4, 24)
    db.plot_future_salary_increase(5, 24)
