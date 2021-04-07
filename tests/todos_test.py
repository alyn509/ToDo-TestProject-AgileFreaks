import unittest
from todos import ToDoList


class MyTestCase(unittest.TestCase):
    def test_ListAll_WithNoToDos_ReturnEmptyListWith0Active(self):
        tds = ToDoList()
        expected_result = {"details": {"activeToDos": 0}, "items": []}
        self.assertEqual(expected_result, tds.list_all())

    def test_ListAllActive_With2Active_ReturnListWith2Active(self):
        tds = ToDoList()
        tds.append("make coffee")
        tds.append("toast_bread")
        expected_result = {"details": {"activeToDos": 2}, "items": [{"id": 1, "name": "make coffee", "status": "active"}, {"id": 2, "name": "toast_bread", "status": "active"}]}
        self.assertEqual(expected_result, tds.list_all('active'))

    def test_ListAllInactive_With2Active_ReturnEmptyListWith2Active(self):
        tds = ToDoList()
        tds.append("make coffee")
        tds.append("toast_bread")
        expected_result = {"details": {"activeToDos": 2}, "items": []}
        self.assertEqual(expected_result, tds.list_all('inactive'))


if __name__ == '__main__':
    unittest.main()
