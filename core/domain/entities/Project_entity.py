from datetime import datetime

class ProjectEntity:
    def __init__(self, id: int, title: str, description: str, coding_guidelines: str, readme: str,
                 owner_id: int, created_at: datetime):
        self.id = id
        self.title = title
        self.description = description
        self.coding_guidelines = coding_guidelines
        self.readme = readme
        self.owner_id = owner_id
        self.created_at = created_at
        self.sprints = []
        self.tasks = []