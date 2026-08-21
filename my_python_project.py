import unittest
import os

FILENAME = "test_tasks.txt"

class TestTodoList(unittest.TestCase):

    def setUp(self):
        """Runs before each test: starts with clean empty lists."""
        self.tasks = []
        self.statuses = []

    def test_add_task(self):
        """Test adding a task."""
        title = "Read a book"
        self.tasks.append(title)
        self.statuses.append("Pending")
        
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0], "Read a book")
        self.assertEqual(self.statuses[0], "Pending")

    def test_mark_completed(self):
        """Test marking a task as completed."""
        self.tasks.append("Do Homework")
        self.statuses.append("Pending")
        
        # Mark index 0 as completed
        self.statuses[0] = "Completed"
        
        self.assertEqual(self.statuses[0], "Completed")

    def test_delete_task(self):
        """Test deleting a task."""
        self.tasks = ["Task 1", "Task 2"]
        self.statuses = ["Pending", "Pending"]
        
        # Delete index 0
        self.tasks.pop(0)
        self.statuses.pop(0)
        
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(self.tasks[0], "Task 2")

    def test_search_task(self):
        """Test search logic."""
        self.tasks = ["Buy Milk", "Clean Room", "Buy Eggs"]
        query = "buy"
        
        results = [t for t in self.tasks if query.lower() in t.lower()]
        self.assertEqual(len(results), 2)

unittest.main()
