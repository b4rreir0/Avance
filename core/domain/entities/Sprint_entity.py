from datetime import date

class SprintEntity:
    def __init__(self, id: int, name: str, goal: str, start_date: date, end_date: date, project_id: int):
        self.id = id
        self.name = name
        self.goal = goal
        self.start_date = start_date
        self.end_date = end_date
        self.project_id = project_id
        self.tasks = []