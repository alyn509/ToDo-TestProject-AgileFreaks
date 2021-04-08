import unittest
from todos import ToDoRepository, Status


class MyTestCase(unittest.TestCase):
    def test_ListAll_WithNoToDos_ReturnsEmptyList(self):
        tds = ToDoRepository()
        self.assertEqual([], tds.list_all())

    def test_ListAllActive_With2Active_ReturnsListWith2Active(self):
        tds = ToDoRepository()
        tds.add("make coffee")
        tds.add("toast_bread")
        self.assertEqual(2, len(tds.list_all(Status.ACTIVE.value)))
        self.assertEqual(True, all(ele.has_status(Status.ACTIVE.value) for ele in tds.list_all(Status.ACTIVE.value)))

    def test_ListAllActive_With2Active1Inactive_ReturnsListWith2Active(self):
        tds = ToDoRepository()
        tds.add("make coffee")
        tds.add("toast_bread")
        tds.add("wash dishes", Status.INACTIVE.value)
        self.assertEqual(2, len(tds.list_all(Status.ACTIVE.value)))
        self.assertEqual(True, all(ele.has_status(Status.ACTIVE.value) for ele in tds.list_all(Status.ACTIVE.value)))

    def test_ListAll_With2Active1Inactive_ReturnsListWith3(self):
        tds = ToDoRepository()
        tds.add("make coffee")
        tds.add("toast_bread")
        tds.add("wash dishes", Status.INACTIVE.value)
        self.assertEqual(3, len(tds.list_all(Status.ALL.value)))

    def test_ListAllInactive_With2Active_ReturnsEmptyList(self):
        tds = ToDoRepository()
        tds.add("make coffee")
        tds.add("toast_bread")
        self.assertEqual([], tds.list_all(Status.INACTIVE.value))


if __name__ == '__main__':
    unittest.main()
