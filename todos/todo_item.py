from .status import Status


class ToDoItem:

    def __init__(self, identifier: int, name: str, status: str):
        self.id = identifier
        self.name = name
        self.status = status

    def has_status(self, status: str):
        return status == Status.ALL.value or self.status == status

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
        }
