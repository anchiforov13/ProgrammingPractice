from worker import *
from database import WorkerDatabase

if __name__ == "__main__":
    a = WorkerDatabase("text.csv")
    a.search_workers('name', 'Joe')
    a.sort_by_param('surname')