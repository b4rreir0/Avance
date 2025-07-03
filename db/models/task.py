from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    status = Column(String(20), default="todo")
    priority = Column(String(20), default="medium")
    estimated_hours = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    sprint_id = Column(Integer, ForeignKey("sprints.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    assignee_id = Column(Integer, ForeignKey("users.id"))
    parent_task_id = Column(Integer, ForeignKey("tasks.id"))

    # Relaciones (puedes definirlas después)
    # sprint = relationship("Sprint", back_populates="tasks")
    # project = relationship("Project")
    # assignee = relationship("User")
    # subtasks = relationship("Task", back_populates="parent_task", remote_side=[parent_task_id])
    # parent_task = relationship("Task", back_populates="subtasks", remote_side=[id])
    # time_entries = relationship("TimeEntry", back_populates="task")