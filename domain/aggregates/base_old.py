from datetime import datetime


class Entity:
    id: int
    created: datetime
    modified: datetime
    version: int

    def __init__(self, id: int):
        self.id = id
        self.created = datetime.now()
        self.modified = datetime.now()
        self.version = 1
