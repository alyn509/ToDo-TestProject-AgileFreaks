from .todo_item import ToDoItem


class ToDoList:
    def __init__(self):
        self.items = list()

    def append(self, item: str):
        self.items.append(ToDoItem(len(self.items) + 1, item, 'active'))

    def get_active(self):
        return {
            'activeToDos': sum(map(lambda x: x.has_status('active'), self.items))
        }

    def list_all(self, specific: str = "all"):
        return {
            'items': [
                x.serialize() for x in list(filter(lambda x: x.has_status(specific), self.items))
            ],
            'details': self.get_active()
        }
