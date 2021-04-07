class ToDoItem:
    def __init__(self, index: int, name: str, status: str):
        self.id = index
        self.name = name
        self.status = status

    def has_status(self, status: str):
        return status == 'all' or self.status == status

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
        }
