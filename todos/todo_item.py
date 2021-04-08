from .status import Status, ALL


class ToDoItem:

    def __init__(self, identifier: int, name: str, status: str):
        self.id = identifier
        self.name = name
        self.status = status

    def has_status(self, status: str):
        return status == ALL or self.status == status

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
        }
