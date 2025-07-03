from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Sprint(Base):
    __tablename__ = "sprints"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    goal = Column(String(255))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"))

    # Relaciones (puedes definirlas después)
    # tasks = relationship("Task", back_populates="sprint")
    # project = relationship("Project", back_populates="sprints")

    def __repr__(self):
        return f"Sprint(id={self.id}, name={self.name}, goal={self.goal}, start_date={self.start_date}, end_date={self.end_date})"