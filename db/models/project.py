from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relaciones (puedes habilitarlas después)
    # sprints = relationship("Sprint", back_populates="project")
    # tasks = relationship("Task", back_populates="project")

    def __repr__(self):
        return f"<Project(id={self.id}, name={self.name})>"
