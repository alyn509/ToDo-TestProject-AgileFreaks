from .todo_item import ToDoItem
from .status import Status, ALL


class ToDoRepository:
    def __init__(self):
        self.items = list()

    def add(self, item_name, status=Status.ACTIVE.value):
        self.items.append(ToDoItem(len(self.items)+1, item_name, status))

    def list_all(self, specific=ALL):
        return list(x for x in list(filter(lambda x: x.has_status(specific), self.items)))
