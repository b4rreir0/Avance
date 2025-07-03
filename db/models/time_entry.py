from sqlalchemy import Column, Integer, Float, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.base import Base

class TimeEntry(Base):
    __tablename__ = "time_entries"

    id = Column(Integer, primary_key=True, index=True)
    hours = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(Text)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relaciones (puedes definirlas después)
    # task = relationship("Task", back_populates="time_entries")
    # user = relationship("User")

    def __repr__(self):
        return f"<TimeEntry(id={self.id}, hours={self.hours}, date={self.date}, description={self.description})>"