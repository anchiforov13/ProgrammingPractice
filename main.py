from worker import *
from database import WorkerDatabase
import unittest

class WorkerDatabaseTesting(unittest.TestCase):
    database = WorkerDatabase("text.csv")

    def test_search_existing_workers(self):
        search_key = "department"
        search_value = "IT"
        search_results = self.database.search_workers(search_key, search_value)

        self.assertTrue(all(worker.department == search_value for worker in search_results))

    def test_search_nonexisting_workers(self):
        search_key = "department"
        search_value = "ITn't"
        search_results = self.database.search_workers(search_key, search_value)

        self.assertFalse(any(worker.department == search_value for worker in search_results))

    def test_delete_existing_worker(self):
        initial_length = len(self.database.database)
        worker_id_to_delete = self.database.database[0].worker_id
        self.database.delete_worker(worker_id_to_delete)
        updated_length = len(self.database.database)

        self.assertEqual(updated_length, initial_length - 1)
        self.assertTrue(next((w for w in self.database.database if w.worker_id == worker_id_to_delete), None) == None)

    def test_delete_nonexistent_worker(self):
        initial_length = len(self.database.database)
        nonexistent_worker_id = -1
        self.database.delete_worker(nonexistent_worker_id)
        updated_length = len(self.database.database)

        self.assertEqual(updated_length, initial_length)

    def test_delete_last_worker(self):
        initial_length = len(self.database.database)
        last_worker_id = self.database.database[-1].worker_id
        self.database.delete_worker(last_worker_id)
        updated_length = len(self.database.database)

        self.assertEqual(updated_length, initial_length - 1)
        self.assertTrue(next((w for w in self.database.database if w.worker_id == last_worker_id), None) is None)

    def test_delete_twice(self):
        worker_id_to_delete = self.database.database[0].worker_id
        self.database.delete_worker(worker_id_to_delete)
        initial_length = len(self.database.database)

        self.database.delete_worker(worker_id_to_delete)
        updated_length = len(self.database.database)

        self.assertEqual(updated_length, initial_length)

    def test_delete_in_loop(self):
        initial_length = len(self.database.database)

        for worker in self.database.database[:3]:
            self.database.delete_worker(worker.worker_id)

        updated_length = len(self.database.database)

        self.assertEqual(updated_length, initial_length - 3)

if __name__ == "__main__":
    unittest.main()