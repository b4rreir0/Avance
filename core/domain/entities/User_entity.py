class UserEntity:
    def __init__(self, id: int, email: str, name: str = None):
        self.id = id
        self.email = email
        self.name = name
        self.assigned_tasks = []