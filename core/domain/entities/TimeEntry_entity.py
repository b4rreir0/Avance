from datetime import date

class TimeEntryEntity:
    def __init__(self, id: int, hours: float, date: date, description: str, task_id: int, user_id: int):
        self.id = id
        self.hours = hours
        self.date = date
        self.description = description
        self.task_id = task_id
        self.user_id = user_id