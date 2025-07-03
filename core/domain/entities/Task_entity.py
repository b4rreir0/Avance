from datetime import datetime

class TaskEntity:
    def __init__(self, id: int, title: str, description: str, status: str, priority: str,
                 estimated_hours: float, created_at: datetime, sprint_id: int, project_id: int,
                 assignee_id: int, parent_task_id: int = None):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.estimated_hours = estimated_hours
        self.created_at = created_at
        self.sprint_id = sprint_id
        self.project_id = project_id
        self.assignee_id = assignee_id
        self.parent_task_id = parent_task_id
        self.subtasks = []
        self.time_entries = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def add_time_entry(self, time_entry):
        self.time_entries.append(time_entry)